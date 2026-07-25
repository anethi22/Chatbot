"""Prompt-chaining Groq chatbot.

This script demonstrates prompt chaining by making three sequential API calls:
1) Analysis — analyze the user's request (goal, topics, constraints).
2) Plan — produce a concise plan based on the analysis.
3) Final Response — generate the final answer using the analysis and plan.

Prompt chaining differs from zero-shot and few-shot prompting:
- Zero-shot: single instruction, one API call, no examples.
- Few-shot: single instruction plus examples in the prompt, still one API call.
- Prompt chaining: multiple API calls where each step's output is passed to
  the next step; this lets the model iteratively refine or transform content.

Constraints followed: no few-shot examples, no chain-of-thought prompting,
three separate calls, and display all intermediate outputs.
"""

from chatbot_utils import ask_model


def analysis_prompt(user_request: str) -> str:
    """Build the prompt for step 1: analyze the user's request.

    This prompt asks the model to produce a concise analysis identifying the
    main goal, key topics, constraints, and any assumptions. It explicitly
    forbids chain-of-thought or private/internal reasoning.
    """

    return (
        "Please analyze the user's request and provide a concise Analysis that"
        " lists:\n- Main goal\n- Key topics\n- Constraints\n- Assumptions to clarify (if any)."
        "\nDo NOT provide chain-of-thought or internal monologue; only return the"
        " brief Analysis.\n\nUser request:\n" + user_request
    )


def plan_prompt(analysis: str) -> str:
    """Build the prompt for step 2: create a plan based on the analysis.

    The plan should be concise, actionable, and numbered when appropriate.
    """

    return (
        "Using the Analysis below, create a concise Plan to accomplish the user's"
        " request. The Plan should be a short list of clear steps or sub-tasks."
        " Do NOT include chain-of-thought.\n\nAnalysis:\n" + analysis
    )


def final_prompt(analysis: str, plan: str, user_request: str) -> str:
    """Build the prompt for step 3: generate the final response.

    This prompt provides the Analysis and Plan to the model and asks for the
    final, user-facing response. No chain-of-thought should be included.
    """

    return (
        "Using the Analysis and Plan below, produce the Final Response to the user."
        " Keep it clear and directly address the user's request. Do NOT include"
        " hidden chain-of-thought.\n\nAnalysis:\n"
        + analysis
        + "\n\nPlan:\n"
        + plan
        + "\n\nUser request:\n"
        + user_request
    )


def main():
    print("Prompt-chaining Groq chatbot. Type 'quit' to exit.")

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

        # Step 1: Analysis
        step1_prompt = analysis_prompt(user_input)
        analysis = ask_model(step1_prompt)

        print("\n--- Stage 1: Analysis ---")
        print(analysis.strip())

        # Step 2: Plan (uses output of Analysis)
        step2_prompt = plan_prompt(analysis)
        plan = ask_model(step2_prompt)

        print("\n--- Stage 2: Plan ---")
        print(plan.strip())

        # Step 3: Final Response (uses Analysis + Plan)
        step3_prompt = final_prompt(analysis, plan, user_input)
        final_response = ask_model(step3_prompt)

        print("\n--- Stage 3: Final Response ---")
        print(final_response.strip())
        print("\n===============================\n")


if __name__ == "__main__":
    main()
