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
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": "What's the capital of Zimbabwe?"},
            ],
        )
        print("AI:", response.choices[0].message.content)
