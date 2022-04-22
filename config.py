"""
Init settings with common parameters
"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    App's settings
    """

    APP_NAME: str = "EdamamBE"
    EDAMAM_APP_ID: str
    EDAMAM_APP_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
