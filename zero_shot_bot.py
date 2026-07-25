from chatbot_utils import ask_model

ZERO_SHOT_PROMPT = (
    "You are a helpful assistant that answers user questions concisely and helpfully. "
    "Do not ask clarifying questions; answer in plain text.\n\nUser: {user_input}\nAssistant:"
)


def build_prompt(user_input: str) -> str:
    return ZERO_SHOT_PROMPT.format(user_input=user_input)


def main():
    print("Zero-shot Groq chatbot. Type 'quit' to exit.")
    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break

        if not user_input:
            continue
        if user_input.lower() == "quit":
            print("Goodbye.")
            break

        prompt = build_prompt(user_input)
        try:
            response = ask_model(prompt)
        except Exception as e:
            print("Error contacting model:", e)
            continue

        print("Bot:", response.strip())


if __name__ == "__main__":
    main()
