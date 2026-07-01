from app.services.agent import choose_tools
from app.services.tool_registry import TOOLS
from app.services.reflection import reflect


def execute_plan(question, plan):
    """
    Executes the plan by selecting
    and running the required tools.
    """

    tool_names = choose_tools(question)

    print(f"\nSelected Tools: {tool_names}")

    results = []

    for tool_name in tool_names:

        tool = TOOLS.get(tool_name)

        if not tool:
            continue

        print(f"\nExecuting {tool_name}...")

        tool_result = tool(question)

        print(f"{tool_name} Result:")
        print(tool_result)

        # ------------------------
        # REFLECTION
        # ------------------------

        reflection = reflect(
            tool_result["answer"]
        )

        print("\nREFLECTION:")
        print(reflection)

        results.append(
            {
                "tool": tool_name,
                "result": tool_result,
                "reflection": reflection
            }
        )

    return tool_names, results