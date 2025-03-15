from pydantic import BaseModel, ConfigDict
from datetime import datetime

class NoteCreate(BaseModel):
    title: str
    content: str

class NoteUpdate(BaseModel):
    title: str
    content: str

class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    version: int
    created_at: datetime | None
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)