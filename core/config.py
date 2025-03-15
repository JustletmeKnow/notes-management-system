from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str
    GEMINI_API_KEY: str

    model_config = ConfigDict(env_file=".env")

settings = Settings()