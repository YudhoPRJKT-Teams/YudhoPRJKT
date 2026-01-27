from .base_exceptions import ConnectorBaseException

class ClientExceptions:
  class ConnectionError(ConnectorBaseException):
    """Connection Error Message
  
    Args:
        error_msg (str): your error Message
        reason(str, optional): your reason message
    """ 
    