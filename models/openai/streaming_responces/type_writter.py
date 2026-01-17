import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def type_writter_streaming(client, delay=0.02):
    response = client.responses.create(
        model="gpt-4o-mini", input="Write a short scifi story. 50 words.", stream=True
    )
    try:
        for event in response:
            if event.type == "response.output_text.delta":
                for char in event.delta:
                    print(char, end="", flush=True)
                    time.sleep(delay)
    except Exception as e:
        print(f"ERROR {e}")


if __name__ == "__main__":
    type_writter_streaming(client=client)
