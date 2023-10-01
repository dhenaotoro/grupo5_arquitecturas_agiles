import boto3
import json
from src.Queries import Queries
from utils.Constants import Constants
from utils.Response import Response

sqs = boto3.client("sqs", region_name="us-east-1")
sns = boto3.client("sns", region_name="us-east-1")
    
class Service:
    
  def validarCredenciales(form):
    print("USUARIO {} PASSWORD {}".format(form["usuario"], form["password"]))
    try:
      if " " in form["password"]:
        sns.publish(TopicArn=Constants.SNS_ARN, Message=str(Constants.MSG_ALERT.replace("{}", form["usuario"])))
        response = {
          "statusCode": 404,
          "body": json.dumps(Constants.MSG_ALERT.replace("{}", form["usuario"])),
          "headers": {
            "Content-Type": "application/json"
          }
        }
      else:
        query = Queries.validarCredenciales(form["usuario"], form["password"])
        if Response.body["message"] == Constants.MSG_SUCCESS:
          if query["object"]:
              response_body = {"status": 200, "mensaje": Constants.MSG_LOGIN_SUCCESSFUL}
              response = {
                "statusCode": response_body["status"],
                "body": json.dumps(response_body),
                "headers": {
                  "Content-Type": "application/json"
                }
              }
        else:
          response_body = {"status": 404, "mensaje": query["message"]}
          response = {
            "statusCode": response_body["status"],
            "body": json.dumps(response_body),
            "headers": {
              "Content-Type": "application/json"
            }
          }
    except Exception as error:
      lineaError = error.__traceback__
      print({ "ERROR": str(error), "LINEA": str(lineaError.tb_lineno) })
      response = {"status": 404, "mensaje": Constants.MSG_ERROR}
    finally:
      return  response
  