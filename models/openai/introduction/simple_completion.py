import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def run(client):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {
                "role": "user",
                "content": "Explain what a Large Language Model is in one sentence.",
            },
        ],
    )

    print("AI:", response.output_text)
    for item in response.output:
        if item["type"] == "message":
            for block in item["content"]:
                if block["type"] == "output_text":
                    print(block["text"])


if __name__ == "__main__":
    run(client=client)


# OLD Chat completions API

# def run(client):
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are a helpful AI assistant."},
#             {
#                 "role": "user",
#                 "content": "Explain what a Large Language Model is in one sentence.",
#             },
#         ],
#     )

#     print("AI:", response.choices[0].message.content)
#     print("\nTokens used:")
#     print(" Input:", response.usage.prompt_tokens)
#     print(" Output:", response.usage.completion_tokens)
#     print(" Total:", response.usage.total_tokens)
