Groq Chatbot Collection
======================

This repository contains simple terminal chatbots that demonstrate different
prompting techniques using the Groq API.

Included bots
- `zero_shot_bot.py`: zero-shot prompting (single instruction).
- `few_shot_bot.py`: few-shot prompting with 2–3 example Q/A pairs (Definition / Example / Key Point).
- `chain_of_thought_bot.py`: structured, user-facing reasoning (Approach / Steps / Final Answer / Check). Does NOT reveal hidden chain-of-thought.
- `prompt_chaining_bot.py`: prompt chaining example — three sequential model calls (Analysis → Plan → Final Response).
- `chatbot_utils.py`: shared `ask_model()` helper that calls the Groq API.

Prerequisites

- Python 3.8+
- A Groq API key. Set it in a .env file as GROQ_API_KEY=your_key or export it in your environment.

Install

Run the following to install dependencies (from the repository root):

    python -m pip install -r requirements.txt

Run

Start any bot from the project root. Type `quit` to exit.

zero-shot:
    python zero_shot_bot.py

few-shot:
    python few_shot_bot.py

structured reasoning:
    python chain_of_thought_bot.py

prompt chaining:
    python prompt_chaining_bot.py

Security notes

- Do NOT commit secrets. `.env` is included in `.gitignore`. If you accidentally commit a secret, rotate it immediately.
- The repository history was cleaned to remove the `.env` file — if you pushed a secret previously, rotate that key now.

Files to review

- `chatbot_utils.py` — implement and inspect `ask_model()` for HTTP or library client behavior.
- `zero_shot_bot.py`, `few_shot_bot.py`, `chain_of_thought_bot.py`, `prompt_chaining_bot.py` — each contains comments explaining the prompting pattern used.

Want more?

- I can add CI checks for secret scanning, a pinned `requirements.txt`, or a README badge and usage examples. Tell me which.
