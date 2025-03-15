import pytest
from unittest.mock import create_autospec, MagicMock
from sqlalchemy.orm import Session
from app.database.models.note import Note
from app.schemas.note import NoteCreate, NoteUpdate
from app.crud.notes import create_note, get_note, update_note, delete_note

@pytest.fixture
def mock_db():
    return create_autospec(Session)

def test_create_note(mock_db):
    note_data = NoteCreate(title="Test Title", content="Test Content")
    mock_note = Note(id=1, title="Test Title", content="Test Content")
    mock_db.add.return_value = None
    mock_db.commit.return_value = None
    mock_db.refresh.return_value = None

    result = create_note(mock_db, note_data)

    assert result.title == "Test Title"
    assert result.content == "Test Content"
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()

def test_get_note(mock_db):
    mock_note = Note(id=1, title="Test Title", content="Test Content")
    mock_db.query.return_value.filter.return_value.first.return_value = mock_note

    result = get_note(mock_db, 1)

    assert result.id == 1
    assert result.title == "Test Title"
    assert result.content == "Test Content"
    mock_db.query.assert_called_once_with(Note)

def test_get_note_not_found(mock_db):
    mock_db.query.return_value.filter.return_value.first.return_value = None

    result = get_note(mock_db, 1)

    assert result is None

def test_update_note(mock_db):
    mock_note = Note(id=1, title="Old Title", content="Old Content", version=1)
    note_update_data = NoteUpdate(title="New Title", content="New Content")
    mock_db.query.return_value.filter.return_value.first.return_value = mock_note

    result = update_note(mock_db, 1, note_update_data)

    assert result.title == "New Title"
    assert result.content == "New Content"
    assert result.version == 2
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()

def test_update_note_not_found(mock_db):
    mock_db.query.return_value.filter.return_value.first.return_value = None

    result = update_note(mock_db, 1, NoteUpdate(title="New Title", content="New Content"))

    assert result is None

def test_delete_note(mock_db):
    mock_note = Note(id=1, title="Test Title", content="Test Content")
    mock_db.query.return_value.filter.return_value.first.return_value = mock_note

    result = delete_note(mock_db, 1)

    assert result.id == 1
    assert result.title == "Test Title"
    assert result.content == "Test Content"
    mock_db.delete.assert_called_once_with(mock_note)
    mock_db.commit.assert_called_once()

def test_delete_note_not_found(mock_db):
    mock_db.query.return_value.filter.return_value.first.return_value = None

    result = delete_note(mock_db, 1)

    assert result is None