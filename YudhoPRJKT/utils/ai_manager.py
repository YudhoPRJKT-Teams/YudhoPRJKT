from .log import Log
from ..auth import Auth
from google import genai
from openai import OpenAI

keys = Auth()

class Gemini:
  """Gemini AI Baseclass"""
  def __init__(self) -> None:
    self.genai = genai.Client(api_key=keys.gemini_key)
  async def text(self, prompt: str) -> str:
    try:
      """Google AI Chatbot
  
      Args:
          prompt (str): Your prompt text
  
      Returns:
          str: result answer
      """
      response = await self.genai.aio.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
      )
      return response.text.__str__()
    except Exception as e:
      Log.Error(e.__str__()).Show().Save()
      raise
    finally:
      self.genai.close()
class AzureOpenAI:
  """Azure OpenAI Baseclass"""
  def __init__(self) -> None:
    self.openai = OpenAI(api_key=Auth().github_pat, base_url="https://models.github.ai/inference")
  def text(self, prompt: str) -> str:
    try:
      """AzureOpenAI Chatbot
  
      Args:
          prompt (str): Your prompt text
  
      Returns:
          str: result answer 
      """
      response = self.openai.chat.completions.create(
        messages=[
          {
            'role': 'system',
            'content': 'You are best assistant!',
          },
          {
            'role': 'user',
            'content': prompt
          }
        ],
        temperature=1.0,
        top_p=1.0,
        model='openai/gpt-4.1'
      )
      return response.choices[0].message.content.__str__()
    except Exception as e:
      Log.Error(e.__str__()).Show().Save()
      raise
    finally:
      self.openai.close()
class AI_Manager:
  """AI Manager Baseclasses"""
  def __init__(self) -> None:
    self.gemini = Gemini()
    self.openai = AzureOpenAI()