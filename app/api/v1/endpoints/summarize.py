from fastapi import APIRouter, HTTPException
from app.services.ai_service import summarize_note
from app.database.session import SessionLocal
from app.schemas.summarize import SummarizeRequest

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/summarize/")
def summarize(request: SummarizeRequest):
    """
    Endpoint to summarize the text of a note.

    :param request: Text of the note.
    """
    try:
        summary = summarize_note(request.content)
        return {"The summarized results of this post:": summary}
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))