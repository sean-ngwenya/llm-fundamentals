import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def token_count_streaming(client):
    tokens = 0
    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input="Explain briefly Perry's stages of Development",
            stream=True,
        )

        for event in response:
            if event.type == "response.output_text.delta":
                print(event.delta, end="", flush=True)
            elif event.type == "response.completed":
                tokens = event.response.usage
        print(f"\n\nTotal tokens used: {tokens}")
    except Exception as e:
        print(f"ERROR {e}")


if __name__ == "__main__":
    token_count_streaming(client=client)
