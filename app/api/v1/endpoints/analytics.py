from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.analytics import analyze_notes
from app.database.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/analytics/")
def get_analytics(db: Session = Depends(get_db)):
    try:
        return analyze_notes(db)
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))