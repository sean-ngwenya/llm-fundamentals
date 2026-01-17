import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def run(client):
    conversation = [
        {"role": "system", "content": "You are a Python programming tutor."}
    ]

    prompts = [
        "What is a list comprehension in Python?",
        "Give me an example with numbers.",
        "Now make it filter even numbers only.",
    ]

    for prompt in prompts:
        conversation.append({"role": "user", "content": prompt})
        response = client.responses.create(model="gpt-4o-mini", input=conversation)
        reply = response.output_text
        conversation.append({"role": "assistant", "content": reply})

        print(f"\nUser: {prompt}")
        print(f"AI: {reply}")


if __name__ == "__main__":
    run(client=client)
