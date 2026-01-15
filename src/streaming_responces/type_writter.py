import sys
from pathlib import Path
import time

src_path = Path(__file__).parent.parent
sys.path.insert(0, str(src_path))

from config.openai_client import get_client


def type_writter_streaming(client=get_client(), delay=0.02):
    response = client.responses.create(
        model="gpt-4o-mini", input="Write a short scifi story. 50 words.", stream=True
    )
    try:
        for event in response:
            if event.type == "response.output_text.delta":
                for char in event.delta:
                    print(char, end="", flush=True)
                    time.sleep(delay)
    except Exception as e:
        print(f"ERROR {e}")


if __name__ == "__main__":
    type_writter_streaming()
