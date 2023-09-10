import boto3
import json
from src.Queries import Queries
from utils.Constants import Constants
from utils.Response import Response

sqs = boto3.client("sqs", region_name="us-east-1")
    
class Service:
    
  def validarEmpleado(form):
    try:
      query = Queries.consultarEmpleado(form["nombre"])
      if query["message"] == Constants.MSG_SUCCESS:
        if query["object"]:
          return {"status": 200, "mensaje": Constants.MSG_EMPLOYER_EXISTS}
        else:
          sqs.send_message(
            QueueUrl=Constants.SQS,
            MessageBody=json.dumps(form)
          )
          if isinstance(form['telefono'],int):
            return {"status": 200, "mensaje": Constants.MSG_LAMBDA_2}
          else:
            return {"status": 200, "mensaje": Constants.MSG_LAMBDA_1}
      else:
        return  {"status": 404, "mensaje": query["message"]}
    except:
      return {"status": 404, "mensaje": Constants.MSG_ERROR}