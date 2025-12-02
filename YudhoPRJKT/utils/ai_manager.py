from google import genai
from openai import OpenAI
from ..configs.config import AuthManager
from .create_log import CreateLog
import asyncio


class AImanager:
  class Gemini:
    @classmethod
    def text(cls, prompt: str) -> str:
      if prompt is not None:
        client = genai.Client(api_key=AuthManager.ReadConfig().get('gemini_key'))
        return str(client.models.generate_content(model='gemini-2.5-pro', contents=prompt).text)
      else:
        CreateLog.Error('Please input your prompt!')
        
  class OpenAI:
    class Azure:
      @classmethod
      def text(cls, prompt: str) -> str:
        if prompt is not None:
          client = OpenAI(base_url='https://models.github.ai/inference',api_key=AuthManager.ReadConfig().get('github_pat'))
          response = client.chat.completions.create(
            messages=[
              {
                "role": "system",
                "content": "You are a helpful assistant.",
              },
              {
                "role": "user",
                "content": prompt,
              }
            ],
            temperature=1.0,
            top_p=1.0,
            model='openai/gpt-4.1-mini'
          )
          return str(response.choices[0].message.content)
        else:
          CreateLog.Error('Please input your prompt!')