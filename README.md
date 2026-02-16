# LLM Fundamentals

Hands-on exploration of Large Language Models (LLMs) using multiple providers, structured experimentation, and applied mini-projects.

This repository documents a structured journey into LLM engineering, focusing on:

* OpenAI API
* Anthropic API
* Local models via Ollama
* Function calling
* Structured outputs
* Streaming responses
* Applied mini-projects

The goal is to understand model behavior from first principles while building clean, modular Python utilities that resemble real-world AI engineering workflows.

---

## Repository Structure

```
llm-fundamentals/
├── data/
│   └── raw/
│
├── exercises/
│
├── models/
│   ├── anthropic/
│   └── openai/
│       ├── introduction/
│       ├── streaming_responces/
│       ├── structured_outputs/
│       └── function_calling/
│
├── notebooks/
│   ├── day2_fundamentals.ipynb
│   └── openai_api.ipynb
│
├── projects/
│   ├── function_calling/
│   │   ├── databse_query/
│   │   └── smart_home_controller/
│   └── structured_outputs/
│
├── src/
│   ├── config/
│   ├── openai_client.py
│   ├── ollama_client.py
│   └── openai_utils.py
│
├── main.py
├── pyproject.toml
├── requirements.txt
├── uv.lock
├── LICENSE
└── README.md
```

---

## Core Components

### 1. `models/`

Contains API experiments organized by provider and capability.

#### OpenAI

* Introduction examples
* Streaming response handling
* Structured JSON outputs
* Function calling patterns

#### Anthropic

* Claude-based experiments
* Comparative behavior exploration

---

### 2. `src/`

Reusable client abstractions and utilities.

* `openai_client.py` – Wrapper around OpenAI API calls
* `ollama_client.py` – Local model interaction via Ollama
* `openai_utils.py` – Helper utilities for prompt handling and structured output parsing
* `config/` – Configuration scaffolding

This separation ensures experiments do not mix infrastructure logic with demonstration code.

---

### 3. `projects/`

Applied mini-projects demonstrating real use cases:

* **Function Calling**

  * Database query assistant
  * Smart home controller simulation

* **Structured Outputs**

  * Controlled JSON response workflows

These simulate practical AI system design patterns.

---

### 4. `notebooks/`

Exploratory and conceptual notebooks:

* LLM fundamentals
* API experimentation
* Prompt-response mechanics

Used for interactive experimentation and theory bridging.

---

## Installation

### Option 1 – Using `uv` (Recommended)

```bash
uv sync
```

### Option 2 – Using pip

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file if using API providers:

```
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

If using Ollama locally:

```
ollama run mistral
```

Make sure Ollama is installed and running.

---

## Running the Project

### Main Entry

```bash
python main.py
```

Behavior depends on what is currently configured in `main.py`.

---

### Running Notebooks

```bash
jupyter notebook notebooks/
```

---

## Engineering Focus

This repository emphasizes:

* Provider abstraction
* Clean client wrappers
* Explicit prompt construction
* Deterministic structured outputs
* Tool/function calling workflows
* Local vs hosted model comparison

It is intentionally organized in a modular way to resemble production AI systems, even though it is educational.

---

## Roadmap

* Embeddings and semantic search
* Retrieval-Augmented Generation (RAG)
* Agent-style task orchestration
* Evaluation pipelines
* Cost tracking and token analysis
* Model benchmarking (OpenAI vs Anthropic vs Ollama)

---

## Author

Sean Craig Ngwenya
AI & Software Engineering Student

---

If you are learning LLM engineering and want structured, incremental experimentation, this repository may serve as a practical reference.
