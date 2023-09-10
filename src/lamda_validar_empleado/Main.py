import boto3
import json

def main(event, context):
  try:
    print("INICIO LAMBDA VALIDAR EMPLEADO")
    logger.info(json.loads(event['body']))
    # Send the data to the SQS queue
    response = sqs.send_message(
      QueueUrl=sqs_queue_url,
      MessageBody=json.dumps(json.loads(event['body']))
    )

    respuesta_mensaje = ''
    if isinstance(json.loads(event['body'])['telefono'],int):
      respuesta_mensaje = f'Datos enviados por el lambda almacenar empleado 2\n{response["MessageId"]}'
    else:
      respuesta_mensaje = f'Datos enviados por el lambda almacenar empleado 1\n{response["MessageId"]}'
    return {
      'statusCode': 200,
      'body': respuesta_mensaje,
    }
  except Exception as e:
    linea = e.__traceback__
    print({ "ERROR": str(e), "LINEA": str(linea.tb_lineno)})
    return {
      'statusCode': 500,
      'body': json.dumps({ "ERROR": str(e), "LINEA": str(linea.tb_lineno)})
    }
