def search_users(name=None, DATABASE=None, min_age=None):
    """Search users in the database by name and/or age"""
    if name:
        result = [u for u in DATABASE if name.lower() in u["name"].lower()]
    if min_age:
        result = [u for u in DATABASE if u["age"] >= min_age]

    if name and min_age:
        result = [
            u
            for u in DATABASE
            if name.lower() in u["name"].lower() and u["age"] >= min_age
        ]

    return result


def search_by_id(id=None, DATABASE=None):
    try:
        id = int(id)
        user = next(u for u in DATABASE if u["id"] == id)
    except StopIteration:
        user = f"User {id}Not found"

    except ValueError:
        # ID couldn't be converted to integer
        return {"error": f"Invalid id format: {id}"}
    return user


def get_database_tools():
    return [
        {
            "type": "function",
            "name": "search_users",
            "description": "Search users in the database by name and/or age",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Name of the user to search for",
                    },
                    "min_age": {
                        "type": "integer",
                        "description": "Minimum age of the user to search for",
                    },
                },
            },
        },
        {
            "type": "function",
            "name": "search_by_id",
            "description": "Search user in the database by ID",
            "parameters": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "ID of the user to search for",
                    },
                },
            },
        },
    ]
