"""
Init settings with common parameters
"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    App's settings
    """

    APP_NAME: str = "FlaskAWS_BE"
    HOST: str
    PORT: int
    DEBUG: bool

    class Config:
        env_file = ".env"


settings = Settings()
