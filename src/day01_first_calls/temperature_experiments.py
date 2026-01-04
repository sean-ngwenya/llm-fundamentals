def run(client):
    prompt = "Write a creative one-sentence story about an AI learning to code."

    for temp in [0.0, 0.7, 1.5]:
        print(f"\n[Temperature {temp}]")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=temp,
        )
        print("AI:", response.choices[0].message.content)
