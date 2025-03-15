# AI-Enhanced Notes Management System



This project is a backend API for a note management system with artificial intelligence (AI) integration. The system allows users to create, read, update and delete notes, and use AI to automatically summarize text.



## Key Features



- **CRUD for notes**: Create, read, update, and delete notes.

- **AI Summarization**: Using Gemini API to automatically summarize the text of notes.

- **Analytics**: Retrieve note statistics including total word count, average note length, most frequent words, most common words or phrases, and the 3 longest and shortest notes.



## Implementation



### Project Architecture



The project is implemented using the following technologies and approaches:



- **FastAPI**: Selected as a modern and performant framework to create the API.

- **SQLAlchemy**: Used for database operations, providing flexibility and support for various RDBMSs.

- **Gemini API**: Integration with AI for summarizing text of notes.

- **Pytest**: For writing unit and integration tests, including mocks for external APIs.



### Implementation decisions



1. **Project Structure**:

   - The project is divided into modules (`app`, `tests`, `services`, `models`, etc.) to ensure clean and maintainable code.

   - The use of `SQLAlchemy` makes it easy to switch between different databases (e.g. SQLite for development and PostgreSQL for production).



2. **AI Summarization**:

   - The Gemini API is used to summarize text. This allows you to generate summarized notes with minimal effort.

   - The `summarize_note` function is isolated into a separate module, making it easy to test and replace the AI model in the future.



3. **Analyze**:

   - The `analyze_notes` function uses the `nltk` library to analyze text. It counts the total number of words, average note length, most frequent words, etc.

   - Tests for analyze check if the word count and other metrics are correct.



4. **Testing**:

   - Unit and integration tests are written using `pytest`.

   - Mocks are used to isolate tests from external APIs (e.g. Gemini).

    
    
## Installation and customization



### 1. Cloning a repository



```bash

git clone https://github.com/JustletmeKnow/notes-management-system.git

cd notes-management-system
```



### 2. Dependency installation
   - Make sure you have Python 3.13 or higher installed. Then install the dependencies:

```bash
pip install -r requirements.txt
```



### 3. Launching the application
   - Start the FastAPI application:

```bash
uvicorn app.main:app --reload
```
   - The application will be available at: http://127.0.0.1:8000.