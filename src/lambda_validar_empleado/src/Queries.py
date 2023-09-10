from src.Connection import Connection
from utils.Constants import Constants
from utils.Response import Response

class Queries:
  
  def consultarEmpleado(nombre):
    response = Response()
    try:
      connection = Connection.connectionOpen()
      if connection.body["message"] == Constants.MSG_SUCCESS:
        cursor = connection.object.cursor()
        query = """
          SELECT
            *
          FROM 
          	abcjobs
        	WHERE
        	  nombre = '{}'
        """.format(nombre)
        cursor.execute(query)
        response.body["object"] = cursor.fetchall()
        connection.object.commit()
        response.body["message"] = Constants.MSG_SUCCESS
        Connection.connectionClose(connection.object)
      else:
        response.body["message"] = connection.body["message"]
    except:
      response.body["message"] = Constants.MSG_ERROR
    finally:
      return response.body