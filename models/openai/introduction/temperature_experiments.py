import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def run(client):
    prompt = "Write a creative one-sentence story about an AI learning to code."

    for temp in [0.0, 0.7, 1.5]:
        print(f"\n[Temperature {temp}]")
        response = client.responses.create(
            model="gpt-4o-mini",
            input=[{"role": "user", "content": prompt}],
            temperature=temp,
        )
        print("AI:", response.output_text)


if __name__ == "__main__":
    run(client=client)
