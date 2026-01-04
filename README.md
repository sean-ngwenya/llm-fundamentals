# LLM Fundamentals 🚀
**Learning Large Language Models through Hands-On API Engineering**

---

## 📌 Overview

This repository documents my structured journey into **Large Language Model (LLM) engineering** using the OpenAI API.

It focuses on **first principles**, clean Python architecture, and practical experimentation rather than black-box usage.

The goal is to build a strong foundation for:
- Prompt engineering
- Conversational memory
- Model behavior control
- Future work with agents, tools, and autonomous systems

This repository is **educational and experimental** by design.

---

## 🧠 What This Repository Covers

### ✅ Day 1 – First OpenAI API Calls
- Making chat completions using the OpenAI API
- Understanding system vs user prompts
- Persona and behavior control
- Conversation history (context retention)
- Temperature and randomness control
- Token usage inspection

### ✅ Day 2 – LLM Fundamentals (Notebook)
- Conceptual foundations of LLMs
- Prompt structure and response shaping
- Practical experiments in a Jupyter Notebook
- Interactive exploration of model behavior

---

## 📂 Repository Structure
```
llm-fundamentals/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── notebooks/
│   └── day2_fundamentals.ipynb
│
└── src/
    ├── __init__.py
    │
    ├── config/
    │   ├── __init__.py
    │   └── openai_client.py
    │
    ├── day01_first_calls/
    │   ├── __init__.py
    │   ├── simple_completion.py
    │   ├── system_prompts.py
    │   ├── conversation_memory.py
    │   └── temperature_experiments.py
    │
    └── run_day01.py
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/sean-ngwenya/llm-fundamentals.git
cd llm-fundamentals
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file based on the example:
```bash
cp .env.example .env
```

Add your OpenAI API key:
```ini
OPENAI_API_KEY=your_api_key_here
```

⚠️ **Never commit your `.env` file**

---

## ▶️ Running the Code

### Run Day 1 Experiments
From the project root:
```bash
python3 -m src.run_day01
```

This will sequentially execute:
- Simple completion
- Prompt persona experiments
- Multi-turn conversation memory
- Temperature comparisons

### Open Day 2 Notebook
```bash
jupyter notebook notebooks/day2_fundamentals.ipynb
```

---

## 📓 Notebook: Day 2 – LLM Fundamentals

The Day 2 notebook focuses on:
- Conceptual understanding of LLMs
- Prompt → response mechanics
- Controlled experimentation
- Bridging theory with API behavior

This notebook complements the Python modules by allowing interactive exploration.

---

## 🧩 Design Philosophy

- No hardcoded secrets
- Modular Python packages
- Explicit entry points
- Clear separation between learning stages
- Production-style structure even for experiments

This mirrors real-world AI engineering workflows.

---

## 🚧 What's Coming Next

Planned extensions:
- Prompt engineering patterns
- Few-shot and structured outputs (JSON)
- Embeddings and semantic search
- Tool use and function calling
- Autonomous task execution
- Local vs API-based model comparison

---

## 📜 Disclaimer

- This repository is for **educational purposes only**
- All experiments respect API usage policies
- No sensitive data or credentials are included

---

## 👤 Author

**Sean Craig Ngwenya**  
AI & Software Engineering Student  
Focus: LLMs, automation, intelligent systems

---

⭐ If you find this repository useful or instructive, feel free to star it.
