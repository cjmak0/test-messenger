from datetime import datetime, UTC
from pydantic import BaseModel, Field
from uuid import UUID

class Message(BaseModel):
    id: UUID
    message: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))
    sender: str