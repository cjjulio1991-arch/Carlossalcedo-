import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "NEXUS-6 Ω"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./nexus.db")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

    VECTOR_DB_PATH: str = "./chroma_data"

settings = Settings()
