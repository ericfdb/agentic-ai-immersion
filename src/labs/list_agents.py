"""List all agents in the Azure AI Foundry project."""

from typing import Any, cast

from labs.client import get_project_client


def main():
    print("Authenticating...")
    client = get_project_client()
    print("Fetching agents...")
    agents = client.agents.list()

    found = False
    for agent in agents:
        found = True
        versions = list(client.agents.list_versions(agent_name=agent.name))
        latest = versions[0] if versions else None
        v_count = len(versions)

        print(f"\n{agent.name}")
        print(f"  versions: {v_count}")
        if latest:
            defn = cast(Any, latest.definition)
            print(f"  latest:   v{latest.version}")
            print(f"  model:    {defn.model}")
            print(f"  kind:     {defn.kind}")
            tools = getattr(defn, "tools", None)
            if tools:
                tool_names = [getattr(t, "type", type(t).__name__) for t in tools]
                print(f"  tools:    {', '.join(tool_names)}")
            else:
                print(f"  tools:    none")

    if not found:
        print("No agents found.")


if __name__ == "__main__":
    main()
