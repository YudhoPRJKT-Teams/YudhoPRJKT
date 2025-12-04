import subprocess
import io
import sys
import textwrap
import traceback
import ast
import inspect
from .create_log import CreateLog

class Terminal:
  @classmethod
  def bash(cls, command: str) -> str:
    """Run bash terminal

    Args:
        command (str): Your command bash

    Returns:
        str: error and output bash
    """
    try:
      proc = subprocess.run(
        command,
        shell=True,
        check=True,
        text=True,
        capture_output=True,
      )
      cls.out_bash = proc.stdout or proc.stderr
      return cls.out_bash
    except subprocess.CalledProcessError as e:
      CreateLog.Error(f"Error while use Terminal.bash", str(e))
      return str(e)
  @classmethod
  async def python(cls, command: str) -> str:
    """Run python terminal

    Args:
        command (str): Your command python

    Returns:
        str: error and output python
    """
    corrected_syntax = textwrap.dedent(command)
    output_buffer = io.StringIO()
    stdout = sys.stdout
    stderr = sys.stderr
    sys.stdout = output_buffer 
    sys.stderr = output_buffer
    err_msg = ''
    try:
      parsed = ast.parse(corrected_syntax)
      output_statement = []
      last_expr = None
      for i, s in enumerate(parsed.body):
        if isinstance(s, ast.Expr):
          if i == len(parsed.body):
            last_expr = s
          else:
            output_statement.append(f'print({ast.unparse(s.value)})')
        else:
          output_statement.append(ast.unparse(s))
      syntax_body = '\n'.join(output_statement) + '\n'
      if last_expr:
        expr_syntax = ast.unparse(last_expr.value)
        syntax_body += f'__last_expr = None\n'
      else:
        syntax_body += "__last_expr = None\n"
      func_code = f"""
async def __eval_async():
{textwrap.indent(syntax_body, '    ')}
    if callable(__last_expr):
        result = __last_expr()
        if result is not None:
          print(result)
        elif __last_expr is not None:
          print(__last_expr)
"""

      caller_frame = inspect.stack()[1].frame
      exec_globals = caller_frame.f_globals.copy()
      exec_locals = caller_frame.f_locals.copy()
      exec_globals.update(globals())
      exec(func_code, exec_globals, exec_locals)
      await exec_locals['__eval_async']()
    except Exception as e:
      err_msg = f"{type(e).__name__}: {e}"
      # err_msg = traceback.format_exc()
    finally:
      sys.stdout = stdout
      sys.stderr = stderr
    return output_buffer.getvalue() + (err_msg if err_msg else '')