import json
from src.Service import Service
from utils.Constants import Constants

def main(event, context):
  try:
    print("INICIO DE LOGIN")
    response = Service.validarCredenciales(event)
  except:
    response_body = {"status": 404, "mensaje": Constants.MSG_ERROR}
    response = {
        "statusCode": response_body["status"],
        "body": json.dumps(response_body),
        "headers": {
          "Content-Type": "application/json",
        }
    }
    
  finally:
    return response