import psycopg2
import boto3
import json
import logging
from os import environ

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Database connection parameters
_LAMBDA_SSM_RESOURCE = { "db_host" : environ.get("DATABASE_CONNECTION", "NONE"),
                         "db_port": environ.get("PORT", "NONE"),
                         "db_name": environ.get("DATABASE_NAME", "NONE"),
                         "db_user": environ.get("USER_NAME","NONE"),
                         "db_password": environ.get("PASSWORD","NONE")}

# Initialize SQS client
sqs = boto3.client('sqs', region_name='us-east-1')  # Specify your AWS region

# SQS queue URL
sqs_queue_url = 'https://sqs.us-east-1.amazonaws.com/369959456076/ABCJobsMensajesFallidosSQS'  # Replace with your SQS queue URL

def insert_data_into_postgres(data):
    try:
        # Establish a connection to the PostgreSQL database
        logger.debug(data)
        conn = psycopg2.connect(
            host=_LAMBDA_SSM_RESOURCE["db_host"],
            port=_LAMBDA_SSM_RESOURCE["db_port"],
            database=_LAMBDA_SSM_RESOURCE["db_name"],
            user=_LAMBDA_SSM_RESOURCE["db_user"],
            password=_LAMBDA_SSM_RESOURCE["db_password"],
        )

        # Create a cursor object
        cursor = conn.cursor()

        

        # Insert data into the PostgreSQL database
        insert_query = """
            INSERT INTO abcjobs (nombre, edad, telefono, ciudad)
            VALUES (%s, %s, %s, %s)
            """
        cursor.execute(
            insert_query,
            (
                data['nombre'],
                data['edad'],
                data['telefono'],
                data['ciudad'],
            ),
        )
        
        # Commit the changes to the database
        conn.commit()

        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        print('FINAL DEL PROCESO LAMBDA ALMACENAR EMPLEADO 2')
        logger.debug('FINAL DEL PROCESO LAMBDA ALMACENAR EMPLEADO 2')
    except Exception as e:
        print(f'Error: {e}')

def lambda_handler(event, context):
    # Process SQS messages
    for record in event['Records']:
        # Extract the message body from the SQS record
        message_body = json.loads(record['body'])
        
        # Insert the data into the PostgreSQL database
        insert_data_into_postgres(message_body)

    return {
        'statusCode': 200,
        'body': 'Data inserted into the PostgreSQL database successfully'
    }
