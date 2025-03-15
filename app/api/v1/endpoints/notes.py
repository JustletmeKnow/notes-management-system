from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.notes import create_note, get_note, update_note, delete_note
from app.schemas.note import NoteCreate, NoteUpdate, NoteResponse
from app.database.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/notes/", response_model=NoteResponse)
def create_note_endpoint(note: NoteCreate, db: Session = Depends(get_db)):
    try:
        return create_note(db, note)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/notes/{note_id}", response_model=NoteResponse)
def read_note_endpoint(note_id: int, db: Session = Depends(get_db)):
    note = get_note(db, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.put("/notes/{note_id}", response_model=NoteResponse)
def update_note_endpoint(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)):
    return update_note(db, note_id, note)


@router.delete("/notes/{note_id}")
def delete_note_endpoint(note_id: int, db: Session = Depends(get_db)):
    return delete_note(db, note_id)