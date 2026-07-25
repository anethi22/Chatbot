"""Few-shot Groq chatbot.

This script demonstrates few-shot prompting: it includes 2-3 example
question-and-answer pairs that teach the model to respond in the
consistent format: Definition / Example / Key Point.

The few-shot examples are embedded in `FEW_SHOT_PROMPTS` below. They are
concatenated with the user's actual question and then sent to `ask_model()`
from `chatbot_utils.py`.

Important: the examples are not chain-of-thought; they are concise Q/A pairs
that show the desired output structure. The model sees these examples and
is expected to mimic their format when answering the user's question.
"""

from chatbot_utils import ask_model


# ----------------------
# Few-shot example block
# ----------------------
# The examples below are the few-shot demonstrations. They show the model
# exactly how an answer should be structured: three labeled sections
# ('Definition', 'Example', 'Key Point'). Placing them before the user's
# question biases the model to follow the same structure for new inputs.
FEW_SHOT_EXAMPLES = """
Question: What is recursion?
Answer:
Definition: Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem.
Example: A factorial function where factorial(n) calls factorial(n-1) until reaching 1.
Key Point: Use a base case to stop the recursion and ensure progress toward it.

Question: What is polymorphism in object-oriented programming?
Answer:
Definition: Polymorphism allows objects of different types to be treated through the same interface, letting methods behave differently depending on the object's type.
Example: A `draw()` method that renders different shapes (circle, square) when called on different shape instances.
Key Point: Polymorphism promotes flexible and extensible code by relying on common interfaces.

Question: What is memoization?
Answer:
Definition: Memoization is an optimization technique that caches the results of expensive function calls to avoid repeated computation.
Example: Caching Fibonacci numbers so each value is computed once and reused.
Key Point: Memoization trades memory for time to speed up repeated computations.
"""


def build_prompt(user_question: str) -> str:
    """Construct the prompt by combining the few-shot examples with the user's question.

    The prompt explicitly instructs the model to follow the same three-part
    answer structure and to avoid chain-of-thought or extraneous commentary.
    """

    instruction = (
        "Answer the user's question using the exact three labeled sections:"
        "\nDefinition\nExample\nKey Point. Do NOT include chain-of-thought or additional commentary."
    )

    # The few-shot examples come first (demonstrations). After these examples
    # we append the instruction and the user's actual question so the model
    # responds in the demonstrated format.
    prompt = "\n".join([
        FEW_SHOT_EXAMPLES.strip(),
        "",  # blank line for readability
        instruction,
        "",  # blank line before user's question
        f"Question: {user_question}",
        "Answer:",
    ])

    return prompt


def main():
    print("Few-shot Groq chatbot. Type 'quit' to exit.")

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

        # Send the complete few-shot prompt to the model using the shared helper.
        # The model receives the examples first, then the user's question, which
        # nudges it to mimic the examples' format in its response.
        response = ask_model(prompt)

        # Print the model's full response (expected to contain Definition/Example/Key Point)
        print("Bot:\n" + response.strip())


if __name__ == "__main__":
    main()
