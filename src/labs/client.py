"""Shared Azure AI client setup. Every lab imports from here."""

import os
import warnings
from pathlib import Path

from azure.ai.projects import AIProjectClient
from azure.identity import InteractiveBrowserCredential
from dotenv import load_dotenv

warnings.filterwarnings("ignore", message="response_mode='form_post'", module="msal")


load_dotenv(Path(__file__).resolve().parents[2] / ".env")

# Create credential object
TENANT_ID = os.environ["TENANT_ID"]

PROJECT_ENDPOINT = os.environ["AI_FOUNDRY_PROJECT_ENDPOINT"]
MODEL = os.environ.get("AZURE_AI_MODEL_DEPLOYMENT_NAME", "gpt-4o-mini")


#
def get_project_client() -> AIProjectClient:
    credential = InteractiveBrowserCredential(tenant_id=TENANT_ID)
    return AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=credential)
