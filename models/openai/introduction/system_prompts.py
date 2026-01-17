import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def run(client):
    tests = [
        ("Helpful assistant", "You are a helpful assistant."),
        (
            "History expert",
            "You are a Zimbabwean history expert who speaks passionately.",
        ),
        ("Concise mode", "Respond in exactly one sentence."),
    ]

    for name, system_prompt in tests:
        print(f"\n[{name}]")
        response = client.responses.create(
            model="gpt-4o-mini",
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": "What's the capital of Zimbabwe?"},
            ],
        )
        print("AI:", response.output_text)


if __name__ == "__main__":
    run(client=client)
