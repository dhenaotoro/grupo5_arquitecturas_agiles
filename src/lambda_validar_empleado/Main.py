import json
from src.Service import Service
from utils.Constants import Constants

def main(event, context):
  try:
    print("INICIO DE PROCESO")
    response = Service.validarEmpleado(event)
  except:
    response = {"status": 404, "mensaje": Constants.MSG_ERROR}
  finally:
    return response