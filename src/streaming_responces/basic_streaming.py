import sys
from pathlib import Path

# Add the src directory to the Python path
src_path = Path(__file__).parent.parent.parent / "src"
sys.path.insert(0, str(src_path))
# Now you can import openai_client
from config.openai_client import get_client


def basic_streaming(client=get_client()):
    response = client.responses.create(
        model="gpt-4o-mini", input="Write a short scifi story. 300 words.", stream=True
    )
    try:
        for event in response:
            if event.type == "response.output_text.delta":
                print(event.delta, end="", flush=True)

    except Exception as e:
        print(f"ERROR => {e}")


if __name__ == "__main__":
    basic_streaming()
