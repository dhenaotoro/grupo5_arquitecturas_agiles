import psycopg2
import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Database connection parameters
db_host = 'database-abcjobs.c9eflzbfr7ql.us-east-1.rds.amazonaws.com'
db_port = 5432
db_name = 'postgres'
db_user = 'postgres'
db_password = 'abcjobsdb'

# Initialize SQS client
sqs = boto3.client('sqs', region_name='us-east-1')  # Specify your AWS region

# SQS queue URL
sqs_queue_url = 'https://sqs.us-east-1.amazonaws.com/369959456076/ABCJobsSQS'  # Replace with your SQS queue URL

def insert_data_into_postgres(data):
    try:
        # Establish a connection to the PostgreSQL database
        
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_password,
        )

        # Create a cursor object
        cursor = conn.cursor()

        # Insert data into the PostgreSQL database
        if isinstance(data['telefono'], int):
            insert_query = """
                INSERT INTO abcjobs (nombre, edad, telefono, ciudad)
                    VALUES (%s, %s, %s::integer, %s)
                """
        else:
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

        print('FINAL DEL PROCESO LAMBDA ALMACENAR EMPLEADO 1')
        logger.debug('FINAL DEL PROCESO LAMBDA ALMACENAR EMPLEADO 1')
            
    except Exception as e:
        # Initialize SQS client
        sqs = boto3.client('sqs', region_name='us-east-1')  # Specify your AWS region
        sqs_queue_url_fallido = 'https://sqs.us-east-1.amazonaws.com/369959456076/ABCJobsMensajesFallidosSQS'  # Replace with your SQS queue URL
        logger.debug(data)
        # Send the data to the SQS queue
        response = sqs.send_message(
            QueueUrl=sqs_queue_url_fallido,
            MessageBody=json.dumps(data)
        )
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