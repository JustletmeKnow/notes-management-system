from sqlalchemy.orm import Session
from app.database.models.note import Note
from app.schemas.note import NoteCreate, NoteUpdate


def create_note(db: Session, note: NoteCreate):
    db_note = Note(title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def get_note(db: Session, note_id: int):
    return db.query(Note).filter(Note.id == note_id).first()


def update_note(db: Session, note_id: int, note: NoteUpdate):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note:
        db_note.title = note.title
        db_note.content = note.content
        db_note.version += 1
        db.commit()
        db.refresh(db_note)
    return db_note


def delete_note(db: Session, note_id: int):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note:
        db.delete(db_note)
        db.commit()
    return db_note