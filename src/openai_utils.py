import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def run(messages=None, tools=None, tool_choice="auto", store=True):
    # API call - AI decides if it needs to call a function
    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=messages,
            tools=tools,  # Give AI access to tools
            tool_choice=tool_choice,  # Let AI decide when to use them
        )
    except Exception as e:
        print("Error during API call:", e)
        return None
    return response
