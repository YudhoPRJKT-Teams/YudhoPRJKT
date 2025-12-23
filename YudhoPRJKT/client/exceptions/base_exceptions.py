class BaseError(Exception):
  def __init__(self, message: str, reason: str | None = None, status_code: int | None = None):
    """Base Exceptions 

    Args:
        message (str): Error Message
        reason (str | None, optional): Reason above error. Defaults to None.
        status_code (int | None, optional): error code. Defaults to None.
    """
    self.message = message
    self.reason = reason
    self.status_code = status_code
    super().__init__(self.__str__())
  
  def __str__(self) -> str:
    p = [self.message]

    if self.reason:
      p.append(f'Reason: {self.reason}')
    if self.status_code is not None:
      p.append(f'Status Code: {self.status_code}')
    return '\n'.join(p)