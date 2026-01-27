class ConnectorBaseException(Exception):
  def __init__(self, error_msg: str, reason: str | None = None, status_code: int | None = 0):
    self.error_msg = error_msg
    self.reason = reason
    self.status_code = status_code
    if reason:
      if status_code == 0:
        message = f"{error_msg}\nReason: {reason}"
      else:
        message = f"{error_msg}\nReason: {reason}\nStatus Code: {status_code}"
    else:
      message = error_msg
    super().__init__(message)