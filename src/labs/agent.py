"""Reusable helpers for creating agents and running conversations."""

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

from labs.client import MODEL


def create_agent(
    project_client: AIProjectClient,
    name: str,
    instructions: str,
    model: str | None = None,
):
    return project_client.agents.create_version(
        agent_name=name,
        definition=PromptAgentDefinition(
            model=model or MODEL,
            instructions=instructions,
        ),
    )


def ask(project_client: AIProjectClient, agent, question: str, verbose: bool = False) -> str | None:
    openai_client = project_client.get_openai_client()
    response = openai_client.responses.create(
        extra_body={
            "agent_reference": {
                "type": "agent_reference",
                "name": agent.name,
                "version": agent.version,
            }
        },
        input=question,
    )

    if verbose:
        for item in response.output:
            if item.type == "code_interpreter_call":
                print(f"  [tool] code_interpreter (status: {item.status})")
                if item.code:
                    print(f"  [code]\n{item.code}")
                if item.outputs:
                    for out in item.outputs:
                        if out.type == "logs":
                            print(f"  [result] {out.logs}")

    return response.output_text
