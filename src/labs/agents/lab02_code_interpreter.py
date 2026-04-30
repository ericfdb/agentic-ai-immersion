"""Lab 2: Code Interpreter — Python execution sandbox."""

from azure.ai.projects.models import CodeInterpreterTool, PromptAgentDefinition

from labs.agent import ask
from labs.client import MODEL, get_project_client

INSTRUCTIONS = """
version2
You are a helpful data analyst assistant.
When answering questions, write and execute Python code to compute accurate results.
Always show your work — include the code you ran and explain the output.
"""

QUESTIONS = [
    "What is the 15th Fibonacci number? Show me the sequence up to that point.",
    "Calculate the compound interest on $10,000 at 5% annual rate over 10 years, compounded monthly.",
    "Generate the first 20 prime numbers and tell me their sum.",
]


def main():
    client = get_project_client()
    print("Connected to Azure AI Foundry")

    agent = client.agents.create_version(
        agent_name="code-interpreter-testinglab2",
        definition=PromptAgentDefinition(
            model=MODEL,
            instructions=INSTRUCTIONS,
            # HOW WE ADD TOOLS
            tools=[CodeInterpreterTool()],
        ),
    )
    print(f"Created agent: {agent.name} v{agent.version}")

    for q in QUESTIONS:
        print(f"\n{'=' * 60}")
        print(f"Q: {q}\n")
        answer = ask(client, agent, q, verbose=True)
        print(f"A: {answer}")


if __name__ == "__main__":
    main()
