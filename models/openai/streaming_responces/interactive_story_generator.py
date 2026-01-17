import time
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def conversation():
    # genre = input("Enter a Genre (Scifi/Mystery/Fantacy)")
    genre = "Scifi"
    if not genre:
        genre = "Scifi"

    messages = [
        {"role": "system", "content": "You are a creative story generator."},
        {
            "role": "user",
            "content": f"Generate an interactive short story in the {genre} of not more than 100 words. After every 50 words, ask the user to choose between two options to continue the story.",
        },
    ]
    return messages


def stream_chat(response, delay=0.02):
    for event in response:
        if event.type == "response.output_text.delta":
            for char in event.delta:
                print(char, end="", flush=True)
                time.sleep(delay)
        elif event.type == "response.completed":
            usage = event.response.usage
    return usage


def chat(client, messages, stream=True):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=messages,
        stream=stream,
    )
    return response


def total_tokens(usage):
    print(f"\n\nTotal tokens: {usage.total_tokens}")
    print(f"Input tokens: {usage.input_tokens}")
    print(f"Output tokens: {usage.output_tokens}")
    print("=" * 35)


def story_gen(client, delay=0.02):
    print("=" * 10 + "STORY GENERATOR" + "=" * 10)

    try:
        messages = conversation()
        response = chat(client, messages, stream=True)
        usage = stream_chat(response, delay=delay)
        total_tokens(usage)

    except Exception as e:
        print(f"ERROR {e}")


if __name__ == "__main__":
    story_gen(client=client)
