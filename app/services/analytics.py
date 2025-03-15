import nltk

from collections import Counter
from sqlalchemy.orm import Session
from app.database.models.note import Note

nltk.download("punkt_tab")


def analyze_notes(db: Session):
    notes = db.query(Note).all()
    if not notes:
        return {}

    total_words = sum(len([word for word in nltk.word_tokenize(note.content) if word.isalnum()]) for note in notes)

    avg_length = total_words / len(notes)

    all_words = " ".join(note.content for note in notes).lower()
    words = nltk.word_tokenize(all_words)
    words = [word for word in words if word.isalnum() and word]
    common_words = Counter(words).most_common(10)

    sorted_notes = sorted(notes, key=lambda x: len(x.content))
    longest_notes = [note.id for note in sorted_notes[-3:]]
    shortest_notes = [note.id for note in sorted_notes[:3]]

    return {
        "total_word_count": total_words,
        "average_note_length": avg_length,
        "most_common_words": common_words,
        "longest_notes": longest_notes,
        "shortest_notes": shortest_notes,
    }