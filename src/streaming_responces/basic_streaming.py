import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def basic_streaming():
    response = client.responses.create(
        model="gpt-4o-mini", input="Write a short scifi story. 300 words.", stream=True
    )
    try:
        for event in response:
            if event.type == "response.output_text.delta":
                print(event.delta, end="", flush=True)

    except Exception as e:
        print(f"ERROR => {e}")


if __name__ == "__main__":
    basic_streaming()
