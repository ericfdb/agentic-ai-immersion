"""Reusable helpers for creating agents and running conversations."""

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

from .client import MODEL


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


def ask(project_client: AIProjectClient, agent, question: str) -> str | None:
    openai_client = project_client.get_openai_client()
    response = openai_client.responses.create(
        extra_body={
            "agent": {
                "type": "agent_reference",
                "name": agent.name,
                "version": agent.version,
            }
        },
        input=question,
    )
    return response.output_text
