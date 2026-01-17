import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def basic_streaming(client):
    response = client.responses.create(
        model="gpt-4o-mini", input="Write a short scifi story. 300 words.", stream=True
    )

    full_response = ""  # To store the complete response
    try:
        for event in response:
            if event.type == "response.output_text.delta":
                print(event.delta, end="", flush=True)
                full_response += event.delta

    except Exception as e:
        print(f"ERROR => {e}")

    return full_response


if __name__ == "__main__":
    message = basic_streaming(client=client)
    print("\n\nFull response received:\n", message)
