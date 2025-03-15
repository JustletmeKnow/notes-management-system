from pydantic import BaseModel


class SummarizeRequest(BaseModel):
    content: str