from src.Connection import Connection
from utils.Constants import Constants
from utils.Response import Response

class Queries:
  
  def validarCredenciales(usuario, password):
    response = Response()
    try:
      connection = Connection.connectionOpen()
      if connection.body["message"] == Constants.MSG_SUCCESS:
        cursor = connection.object.cursor()
        query = "SELECT * FROM abcjobslogin WHERE usuario = '" + usuario + "' AND (password = '"+ password + "')"
        cursor.execute(query)
        response.body["object"] = cursor.fetchall()
        print("ROWS {}".format(response.body["object"]))
        if len(response.body["object"]) == 0:
          # No matching user found, set error message
          response.body["message"] = Constants.MSG_EMPTY
        else:
    
          response.body["message"] = Constants.MSG_SUCCESS
        
        connection.object.commit()
        Connection.connectionClose(connection.object)
      else:
        response.body["message"] = connection.body["message"]
    except:
      response.body["message"] = Constants.MSG_ERROR
    finally:
      return response.body