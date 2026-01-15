import sys
from pathlib import Path
from config.openai_client import get_client

src_path = Path(__file__).parent.parent
sys.path.insert(0, str(src_path))


def token_count_streaming(client=get_client()):
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
    token_count_streaming()
