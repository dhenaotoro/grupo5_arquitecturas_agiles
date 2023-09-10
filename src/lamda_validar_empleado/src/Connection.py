import psycopg2
from utils.Constants import Constants
from utils.Response import Response

class Connection:
    
  def connectionOpen(database):
    response = Response()
    try:
      connection = psycopg2.connect(
        user = Constants.DB_USER,
        password = Constants.DB_PASS,
        host = Constants.DB_SERVER,
        port = Constants.DB_PORT,
        database = database
      )
      response.object = connection
      response.body["message"] = Constants.MSG_SUCCESS
    except:
      response.body["message"] = Constants.MSG_ERROR
    return response
    
  def connectionClose(connection):
    connection.close()