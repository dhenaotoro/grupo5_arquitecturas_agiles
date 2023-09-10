from utils.Constants import Constants

class Response():
  object = ""
  body = {
    "status": False, 
    "code": Constants.STATUS_ERROR, 
    "message": "", 
    "object": []
  }