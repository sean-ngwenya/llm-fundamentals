def run(client):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {
                "role": "user",
                "content": "Explain what a Large Language Model is in one sentence.",
            },
        ],
    )

    print("AI:", response.choices[0].message.content)
    print("\nTokens used:")
    print(" Input:", response.usage.prompt_tokens)
    print(" Output:", response.usage.completion_tokens)
    print(" Total:", response.usage.total_tokens)
