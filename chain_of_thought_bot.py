"""Structured-reasoning Groq chatbot.

This chatbot uses a single, structured prompting style that asks the model to
analyze problems carefully and return a concise, user-facing explanation using
the labeled sections: Approach, Steps, Final Answer, Check.

Notes on prompting styles (comments inside code further explain differences):
- Zero-shot prompting: gives a single instruction with no examples.
- Few-shot prompting: provides example Q/A pairs to demonstrate desired format.
- Structured reasoning prompting (this file): asks the model to present a
  concise, stepwise user-facing explanation in explicit labeled sections. It
  requests careful analysis but explicitly forbids revealing internal
  chain-of-thought or private deliberation.

Do NOT include hidden chain-of-thought. Use one API call per user question.
"""

from chatbot_utils import ask_model


STRUCTURED_INSTRUCTION = (
    "You are a helpful assistant skilled at math, logic, and problem solving. "
    "Analyze the problem carefully and provide a concise, user-facing explanation "
    "using exactly the following labeled sections:\n\n"
    "Approach: (brief strategy in one or two sentences)\n"
    "Steps: (concise, numbered steps or calculations leading to the answer)\n"
    "Final Answer: (the clear final answer only)\n"
    "Check: (a short verification or sanity-check to show the answer is plausible)\n\n"
    "DO NOT provide hidden chain-of-thought, internal monologue, or private "
    "deliberations. Only present the user-facing explanation in the sections above."
)


def build_prompt(user_question: str) -> str:
    """Combine the structured instruction with the user's question.

    This single prompt (no few-shot examples, no chaining) asks the model to
    reason in a structured, user-facing way. It's designed to help with math,
    logic, and problem-solving while preventing disclosure of internal reasoning.
    """

    prompt = "\n\n".join([
        STRUCTURED_INSTRUCTION,
        f"Question: {user_question}",
        "Answer:",
    ])

    return prompt


def main():
    print("Structured-reasoning Groq chatbot. Type 'quit' to exit.")

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

        # Single API call: pass the structured prompt to the shared helper.
        # The model is instructed to give a clear, user-facing sequence of
        # reasoning steps, followed by the final answer and a brief check.
        response = ask_model(prompt)

        # Output the model response as-is; it should contain the labeled sections.
        print("Bot:\n" + response.strip())


if __name__ == "__main__":
    main()
