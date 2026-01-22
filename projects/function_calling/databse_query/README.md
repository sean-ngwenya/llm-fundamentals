# Database Query Agent

A function-calling agent that queries a CSV database using natural language. Built to practice OpenAI's function calling capabilities.

## What It Does

This agent can search through a user database using natural language queries. It intelligently decides which search functions to use based on your question.

**Example queries:**
- "Search users who have id numbers 1, 3, 7"
- "Find all users aged 25"
- "Show me users from New York"
- "Get user with id 5"

## Project Structure
```
database_query/
├── agent.py           # Main agent logic
├── utils.py           # Search functions and tool definitions
├── data/
│   └── users.csv      # Sample user database
├── requirements.txt
└── README.md
```

## How It Works

1. **User asks a question** in natural language
2. **Agent decides which functions to call** (`search_users` or `search_by_id`)
3. **Functions query the database** and return results
4. **Agent synthesizes** the results into a natural language response

## Available Functions

- `search_users()` - Search by name, age, or city
- `search_by_id()` - Look up specific users by their ID numbers

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your OpenAI API key in `.env` at project root:
```
OPENAI_API_KEY=your_key_here
```

3. Run the agent:
```bash
python agent.py
```

## Key Learning

**Important discovery:** When a function returns `None` or generic "not found" messages, the LLM may discard valid results from other function calls. Always return descriptive error messages like `"User {id} not found"` to maintain context of successful operations.

## Dependencies

- `pandas` - CSV data handling
- `openai` - API client (uses Responses API, not Completions)
- `python-dotenv` - Environment variable management

## Concepts Practiced

- OpenAI Function Calling
- Multi-function orchestration
- Error handling in function responses
- CSV data querying with pandas