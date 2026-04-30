"""List all vector stores and their files in the Azure AI Foundry project."""

from labs.client import get_project_client


def main():
    print("Authenticating...")
    client = get_project_client()
    openai_client = client.get_openai_client()

    print("Fetching vector stores...")
    stores = openai_client.vector_stores.list()

    found = False
    for store in stores:
        found = True
        print(f"\n{store.name or '(unnamed)'}")
        print(f"  id:     {store.id}")
        print(f"  status: {store.status}")
        print(f"  files:  {store.file_counts.total} total ({store.file_counts.completed} completed)")

        if store.file_counts.total > 0:
            files = openai_client.vector_stores.files.list(vector_store_id=store.id)
            for f in files:
                print(f"    - {f.id} (status: {f.status})")

    if not found:
        print("No vector stores found.")


if __name__ == "__main__":
    main()
