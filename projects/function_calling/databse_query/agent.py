import pandas as pd
import json
from utils import search_by_id, search_users, get_database_tools
import sys
from pathlib import Path

src_path = Path(__file__).parents[3] / "src"
sys.path.insert(0, str(src_path))

from openai_utils import run


def get_database():
    input_file_path = Path(__file__).parent / "data" / "users.csv"
    data = pd.read_csv(input_file_path)
    return data.to_dict(orient="records")


def ask_database(query=None):
    if not query:
        return "No query provided."

    database = get_database()
    tools = get_database_tools()

    input_messages = [{"role": "user", "content": str(query)}]
    response = run(messages=input_messages, tools=tools)

    tool_calls = [item for item in response.output if item.type == "function_call"]
    if not tool_calls:
        return response.output_text

    for tool_call in tool_calls:
        input_messages.append(tool_call)

    for tool_call in tool_calls:
        function_name = tool_call.name
        function_args = eval(tool_call.arguments)

        if function_name == "search_users":
            function_output = search_users(DATABASE=database, **function_args)
        elif function_name == "search_by_id":
            function_output = search_by_id(DATABASE=database, **function_args)
        else:
            function_output = f"Function {function_name} not recognized."

        input_messages.append(
            {
                "type": "function_call_output",
                "call_id": tool_call.call_id,
                "output": json.dumps(function_output),
            }
        )

    second_response = run(messages=input_messages, tools=tools)

    return second_response.output_text


def main():
    result = ask_database("Search users who have id numbers 1, 3, 7")
    print(result)


# Thing i got stuck on:
# I first used none then Not fouen in the search by id function try except block for StopIteration and the llm returned nothing, the llm disacarded all the valied outputs ih had made form the previous function calls
# I then used "User {id} not found" which worked and retuened the valid users
