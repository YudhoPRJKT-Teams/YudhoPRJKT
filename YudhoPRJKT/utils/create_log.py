from datetime import datetime
from typing import Optional
import os
import inspect

class CreateLog:
  logpath = f'{os.getcwd()}/event.log'
  @classmethod
  def SaveLog(cls):
    """Save Log into file"""
    if not os.path.exists(cls.logpath):
      with open(cls.logpath, 'w') as w:
        w.write(f'{cls.log_pattern}\n')
    else:
      with open(cls.logpath, 'a') as a:
        a.write(f'{cls.log_pattern}\n')
  @classmethod
  def Show(cls):
    """Show Log Message"""
    print(cls.log_pattern)
    return cls

  # Debug Message
  @classmethod
  def Debug(cls, log_message: str, reason: Optional[str] = ""):
    """Create Debug Log

    Args:
        log_message (str): Your log message
        reason (Optional, str): Your optional message 
    """
    now = datetime.now()
    day_name = now.strftime('%A')
    formatted_time = now.strftime('%d-%B-%Y %I:%M:%S %p')
    call_frame = inspect.stack()[1]
    get_running_file = os.path.basename(call_frame.filename).replace('.py', '')
    if reason == "":
      cls.log_pattern = f"{day_name} {formatted_time} DEBUG {get_running_file} - {log_message}"
      return cls
    else:
      cls.log_pattern = f"{day_name} {formatted_time} DEBUG {get_running_file} - {log_message} || Reason: {reason}"
      return cls    
  @classmethod
  def Info(cls, log_message: str, reason: Optional[str] = ""):
    """Create Info Log

    Args:
        log_message (str): Your log message
        reason (Optional, str): Your optional message 
    """
    now = datetime.now()
    day_name = now.strftime('%A')
    formatted_time = now.strftime('%d-%B-%Y %I:%M:%S %p')
    call_frame = inspect.stack()[1]
    get_running_file = os.path.basename(call_frame.filename).replace('.py', '')
    if reason == "":
      cls.log_pattern = f"{day_name} {formatted_time} INFO {get_running_file} - {log_message}"
      return cls
    else:
      cls.log_pattern = f"{day_name} {formatted_time} INFO {get_running_file} - {log_message} || Reason: {reason}"
      return cls
    
  @classmethod
  def Warning(cls, log_message: str, reason: Optional[str] = ""):
    """Create Warning Log

    Args:
        log_message (str): Your log message
        reason (Optional, str): Your optional message 

    """
    now = datetime.now()
    day_name = now.strftime('%A')
    formatted_time = now.strftime('%d-%B-%Y %I:%M:%S %p')
    call_frame = inspect.stack()[1]
    get_running_file = os.path.basename(call_frame.filename).replace('.py', '')
    if reason == "":
      cls.log_pattern = f"{day_name} {formatted_time} WARNING {get_running_file} - {log_message}"
      return cls
    else:
      cls.log_pattern = f"{day_name} {formatted_time} WARNING {get_running_file} - {log_message} || Reason: {reason}"
      return cls
    
  @classmethod
  def Error(cls, log_message: str, reason: Optional[str] = ""):
    """Create Error Log

    Args:
        log_message (str): Your log message
        reason (Optional, str): Your optional message 
    """
    now = datetime.now()
    day_name = now.strftime('%A')
    formatted_time = now.strftime('%d-%B-%Y %I:%M:%S %p')
    call_frame = inspect.stack()[1]
    get_running_file = os.path.basename(call_frame.filename).replace('.py', '')
    if reason == "":
      cls.log_pattern = f"{day_name} {formatted_time} ERROR {get_running_file} - {log_message}"
      return cls
    else:
      cls.log_pattern = f"{day_name} {formatted_time} ERROR {get_running_file} - {log_message} || Reason: {reason}"
      return cls
        
  @classmethod
  def Critical(cls, log_message: str, reason: Optional[str] = ""):
    """Create Critical Log

    Args:
        log_message (str): Your log message
        reason (Optional, str): Your optional message 
    """
    now = datetime.now()
    day_name = now.strftime('%A')
    formatted_time = now.strftime('%d-%B-%Y %I:%M:%S %p')
    call_frame = inspect.stack()[1]
    get_running_file = os.path.basename(call_frame.filename).replace('.py', '')
    if reason == "":
      cls.log_pattern = f"{day_name} {formatted_time} CRITICAL {get_running_file} - {log_message}"
      return cls
    else:
      cls.log_pattern = f"{day_name} {formatted_time} CRITICAL {get_running_file} - {log_message} || Reason: {reason}"
      return cls