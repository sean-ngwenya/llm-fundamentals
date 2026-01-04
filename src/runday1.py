from src.config.openai_client import get_client
from src.day01_first_calls import (
    simple_completion,
    system_prompts,
    conversation_memory,
    temperature_experiments,
)


def main():
    client = get_client()

    print("=" * 70)
    print("DAY 1: FIRST OPENAI API CALLS")
    print("=" * 70)

    simple_completion.run(client)
    system_prompts.run(client)
    conversation_memory.run(client)
    temperature_experiments.run(client)

    print("\n✅ DAY 1 COMPLETE")


if __name__ == "__main__":
    main()
