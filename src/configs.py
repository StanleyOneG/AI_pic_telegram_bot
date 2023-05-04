"""Module for project configurations."""


from dotenv import load_dotenv
from pydantic import BaseSettings, Field

load_dotenv()


class Telegram(BaseSettings):
    """Class for telegram token."""

    token: str = Field(..., env="TOKEN", alias="token")


class Settings(BaseSettings):
    """Class for project configurations."""

    telegram = Telegram()


settings = Settings()
