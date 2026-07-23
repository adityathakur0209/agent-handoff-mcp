from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

from pathlib import Path
from datetime import datetime
import os
import requests
import time

load_dotenv()

mcp = FastMCP("Backstory MCP")


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
    Saves the generated HTML into the OneDrive synced folder
    and triggers the Power Automate flow.
    """

    one_drive_folder = os.getenv("ONEDRIVE_FOLDER")
    flow_url = os.getenv("POWER_AUTOMATE_URL")

    if not one_drive_folder:
        raise Exception("ONEDRIVE_FOLDER not configured in .env")

    folder_path = Path(one_drive_folder)
    folder_path.mkdir(parents=True, exist_ok=True)

    account_name = metadata.get("account_name", "Unknown").replace("/", "-")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{account_name}_{timestamp}.html"

    file_path = folder_path / filename

    file_path.write_text(
        html,
        encoding="utf-8"
    )

    # Give OneDrive a few seconds to sync
    time.sleep(5)

    folder_name = folder_path.name

    flow_triggered = False
    flow_response_status = None
    flow_response_body = None

    if flow_url:

        payload = {
            "file_name": filename,
            "folder": folder_name,
            "metadata": metadata
        }

        try:

            response = requests.post(
                flow_url,
                json=payload,
                timeout=60
            )

            flow_response_status = response.status_code
            flow_response_body = response.text

            if response.ok:
                flow_triggered = True

        except Exception as e:

            flow_response_body = str(e)

    return {
        "success": True,
        "file_name": filename,
        "folder": folder_name,
        "flow_triggered": flow_triggered,
        "flow_response_status": flow_response_status,
        "flow_response_body": flow_response_body,
        "file_path": str(file_path)
    }


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http"
    )