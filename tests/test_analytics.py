import nltk
import pytest

from app.services.analytics import analyze_notes
from app.database.models.note import Note

nltk.download('punkt')
nltk.download('stopwords')


@pytest.mark.parametrize("notes_data, expected_results", [
    (
     [
         {"title": "Note 1", "content": "This is a test note."},
         {"title": "Note 2", "content": "Another test note."},
     ],
     {
         "total_word_count": 8,
         "average_note_length": 4.0,
         "most_common_words": [("note", 2), ("test", 2), ("this", 1), ("is", 1), ("a", 1), ("another", 1)],
         "longest_notes": [2, 1],
         "shortest_notes": [1, 2],
     }
    ),
    (
     [
         {"title": "Note 3", "content": "Just one more note."},
     ],
     {
         "total_word_count": 4,
         "average_note_length": 4.0,
         "most_common_words": [("note", 1), ("just", 1), ("one", 1), ("more", 1)],
         "longest_notes": [1],
         "shortest_notes": [1],
     }
    ),
])
def test_analyze_notes(db, notes_data, expected_results):
    db.query(Note).delete()
    db.commit()
    for data in notes_data:
        note = Note(title=data["title"], content=data["content"])
        db.add(note)
    db.commit()

    analytics = analyze_notes(db)



    assert analytics["total_word_count"] == expected_results["total_word_count"]
    assert analytics["average_note_length"] == expected_results["average_note_length"]
    assert sorted(analytics["most_common_words"]) == sorted(expected_results["most_common_words"])

    assert set(analytics["longest_notes"]) == set(expected_results["longest_notes"])
    assert set(analytics["shortest_notes"]) == set(expected_results["shortest_notes"])
