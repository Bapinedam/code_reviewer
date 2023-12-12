import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

PROMPT = """
        You will receive a file's content as text.
        Generate a code review for the file. Indicate what changes should be made to improve
        its style, performance, readability, and maintainability. If there are
        any reputable libraries that could be introduced to improve the code, suggest them.
        Be kind and constructive. For each suggested change, include the line number to which you are referring
        
        """

filecontent =  """"
                def mistery(x, y):
                    return x ** y
                """
  
messages = [
    {"role": "system", "content": PROMPT},
    {"role": "user", "content": f"Code review the following file: {filecontent}"}
]
        
response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )

print(response.choices[0].message.content)