# Backstory MCP

## Overview

Backstory MCP is a FastMCP server that receives AI-generated Account Handoff HTML documents and publishes them into Salesforce through a Power Automate HTTP flow.

---

## Architecture

```
ChatGPT Agent
        │
        ▼
Backstory MCP
        │
        ▼
Power Automate (HTTP Trigger)
        │
        ▼
Salesforce
```

---

## Features

- Receives HTML account handoff documents
- Sends HTML directly to Power Automate
- Uploads documents into Salesforce Files
- Links files to Salesforce Accounts
- No OneDrive dependency
- No local file storage

---

## Requirements

- Python 3.12+
- FastMCP
- Power Automate
- Salesforce Connected App

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

Create a `.env` file:

```env
POWER_AUTOMATE_URL=<Power Automate HTTP Trigger URL>
```

---

## Run

```bash
source .venv/bin/activate
python server.py
```

---

## MCP Tools

### ping

Returns the server health status.

### publish_account_handoff

Uploads an HTML account handoff document into Salesforce.

Example:

```json
{
  "html": "<html><body>Hello</body></html>",
  "metadata": {
    "account_name": "Test Account",
    "account_id": "001XXXXXXXXXXXX",
    "opportunity_id": "006XXXXXXXXXXXX"
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