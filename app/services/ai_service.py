import os
import google.generativeai as genai
from core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)


def summarize_note(content: str) -> str:
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(f"Summarize this note: {content}")
    return response.text