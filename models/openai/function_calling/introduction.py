import os
import json
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# This is the Python function
def get_current_weather(location, unit="celsius"):
    """Simulated weather function"""
    # In real life, you'd call a weather API here
    weather_data = {
        "London": {"temp": 12, "condition": "cloudy"},
        "Tokyo": {"temp": 15, "condition": "rainy"},
        "New York": {"temp": 8, "condition": "sunny"},
    }

    data = weather_data.get(location, {"temp": 20, "condition": "unknown"})
    return data


def ask_about_weather(messages=None, tools=None, tool_choice="auto", store=True):
    """Function to make the API call asking about weather"""
    # API call - AI decides if it needs to call a function
    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=messages,
            tools=tools,  # Give AI access to tools
            tool_choice=tool_choice,  # Let AI decide when to use them
        )
    except Exception as e:
        print("Error during API call:", e)
        return None
    return response


def tools():
    return [
        {
            "type": "function",
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city, e.g., Tokyo",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The unit of temperature",
                    },
                },
                "required": ["location"],
            },
        }
    ]


def main():
    input_messages = [{"role": "user", "content": "What's the weather like in London?"}]
    response = ask_about_weather(
        messages=input_messages,
        tools=tools(),
        tool_choice="auto",
    )
    # 1. Find the function call
    tool_call = next(
        (item for item in response.output if item.type == "function_call"),
        None,
    )
    # tool_call = response.output[0]

    if not tool_call:
        print("AI:", response.output_text)
        return

    function_name = tool_call.name
    function_args = json.loads(tool_call.arguments)

    print(f"Function to call: {function_name} with args {function_args}")
    input_messages.append(tool_call)
    # 2. Execute the function
    if function_name == "get_current_weather":
        weather_info = get_current_weather(**function_args)
        input_messages.append(
            {
                "type": "function_call_output",  # Special type for function results
                "call_id": tool_call.call_id,  # Match the function call
                "output": json.dumps(weather_info),  # The weather data
            }
        )
        follow_up_response = ask_about_weather(
            messages=input_messages,
            tools=tools(),
            tool_choice="none",  # No more function calls
        )
        print("AI:", follow_up_response.output_text)


if __name__ == "__main__":
    main()
