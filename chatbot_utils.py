import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError(
        "GROQ_API_KEY is not set. Add it to your .env file."
    )

client = Groq(api_key=api_key)


def ask_model(
    prompt: str,
    *,
    model: str = "llama-3.1-8b-instant",
    max_tokens: int = 512,
    temperature: float = 0.0,
) -> str:
    """Send a prompt to Groq and return the model's response."""

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            max_completion_tokens=max_tokens,
            temperature=temperature,
        )

        content = response.choices[0].message.content
    
        if not content:
            return "The model returned an empty response."

        return content.strip()

    except Exception as error:
        return f"Error contacting model: {error}"