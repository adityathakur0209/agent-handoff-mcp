from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

import os
import requests

load_dotenv()

mcp = FastMCP("Agent Handoff MCP")


@mcp.tool()
def ping():
    """
    Simple health check.
    """
    return {
        "status": "alive"
    }


@mcp.tool()
def publish_account_handoff(
    html: str,
    metadata: dict
):
    """
    Sends the generated HTML directly to Power Automate,
    which uploads it into Salesforce.
    """

    flow_url = os.getenv("POWER_AUTOMATE_URL")

    if not flow_url:
        raise Exception("POWER_AUTOMATE_URL not configured in .env")

    account_name = metadata.get("account_name", "Unknown").replace("/", "-")
    filename = f"{account_name}_Handoff.html"

    payload = {
        "html": html,
        "file_name": filename,
        "metadata": metadata
    }

    try:
        response = requests.post(
            flow_url,
            json=payload,
            timeout=120
        )

        # Power Automate may return 504 even if the upload succeeds.
        success = response.status_code in [200, 202, 504]

        return {
            "success": success,
            "status_code": response.status_code,
            "response": response.text,
            "file_name": filename
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http"
    )