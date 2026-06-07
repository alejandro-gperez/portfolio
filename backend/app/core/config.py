"""
Application configuration.

Centralizes application settings and environment variables.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    PROJECT_NAME: str = "Alejandro Portfolio API"

    PROJECT_DESCRIPTION: str = (
        "Backend API powering the Portfolio SaaS platform."
    )

    VERSION: str = "1.0.0"

    API_V1_PREFIX: str = "/api/v1"

    DATABASE_URL: str
    
    class Config:
        env_file = ".env"


settings = Settings()