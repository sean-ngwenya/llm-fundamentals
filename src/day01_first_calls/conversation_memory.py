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
        response = client.chat.completions.create(
            model="gpt-4o-mini", messages=conversation
        )
        reply = response.choices[0].message.content
        conversation.append({"role": "assistant", "content": reply})

        print(f"\nUser: {prompt}")
        print(f"AI: {reply}")
