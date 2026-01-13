from ollama import Client


def get_client() -> Client:
    client = Client(host="http://localhost:11434")
    if not client:
        raise RuntimeError("Could not connect to Ollama server")
    return client
