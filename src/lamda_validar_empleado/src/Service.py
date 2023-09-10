import boto3
from src.Queries import Queries
from utils.Constants import Constants
from utils.Response import Response

sqs = boto3.client("sqs", region_name="us-east-1")
    
class Service:
    
  def validarEmpleado():
    response = Response()
    try:
      query = Queries.consultarEmpleado()
      if query["message"] == Constants.MSG_SUCCESS:
        response.body["code"] = Constants.STATUS_SUCCESS
        if query["object"]:
          response.body["message"] = Constants.MSG_EMPLOYER_EXISTS
          response.body["object"] = data
          response.body["status"] = True
        else:
          response.body["message"] = Constants.MSG_EMPTY
      else:
        response.body["message"] = query["message"]
    except:
      response.body["message"] = Constants.MSG_ERROR
    finally:
      return response