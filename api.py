from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

from server import publish_account_handoff

app = FastAPI(title="Backstory API")


class PublishRequest(BaseModel):
    html: str
    metadata: Dict[str, Any]


@app.get("/")
def health():
    return {
        "status": "ok",
        "service": "Backstory API"
    }


@app.post("/publish")
def publish(request: PublishRequest):

    result = publish_account_handoff(
        html=request.html,
        metadata=request.metadata
    )

    return result