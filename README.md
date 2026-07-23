# Agent Handoff MCP

## Overview

Agent Handoff MCP is a FastMCP server that receives AI-generated Account Handoff HTML documents and publishes them to Salesforce through Power Automate.

---

## Architecture

```
ChatGPT Agent
        │
        ▼
Agent Handoff MCP
        │
        ▼
Power Automate (HTTP Trigger)
        │
        ▼
Salesforce
```

---

## Features

- Receives AI-generated Account Handoff HTML
- Sends HTML directly to Power Automate
- Uploads documents into Salesforce Files
- Links documents to the appropriate Salesforce Account
- No OneDrive dependency
- No local file storage

---

## Requirements

- Python 3.12+
- FastMCP
- Power Automate
- Salesforce

---

## Installation

```bash
git clone <repository-url>
cd Backstory-MCP

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file with:

```env
POWER_AUTOMATE_URL=<Power Automate HTTP Trigger URL>
```

---

## Running the Server

```bash
source .venv/bin/activate
python server.py
```

The MCP server will start on:

```
http://127.0.0.1:8000
```

---

## Available Tools

### `ping`

Returns the server health status.

### `publish_account_handoff`

Publishes an AI-generated Account Handoff HTML document to Salesforce.

Example payload:

```json
{
  "html": "<html><body>...</body></html>",
  "metadata": {
    "account_name": "Test Account",
    "account_id": "001XXXXXXXXXXXX",
    "opportunity_id": "006XXXXXXXXXXXX",
    "generated_by": "Account Handoff Agent"
  }
}
```

---

## Project Structure

```
Backstory-MCP/
│
├── server.py
├── api.py
├── test_publish.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```