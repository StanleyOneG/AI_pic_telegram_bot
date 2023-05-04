"""Module for project configurations."""


from dotenv import load_dotenv
from pydantic import BaseSettings, Field

load_dotenv()


class Telegram(BaseSettings):
    """Class for telegram token."""

    token: str = Field(..., env="TOKEN", alias="token")
    webhook_mode: bool = Field(False, env="WEBHOOK_MODE", alias="webhook_mode")
    host: str = Field(None, env="HOST", alias="host")
    webhook_url: str = Field(None, env="WEBHOOK_URL", alias="webhook_url")
    webhook_port: int = Field(None, env="WEBHOOK_PORT", alias="webhook_port")
    secret_token: str = Field(None, env="SECRET_TOKEN", alias="secret_token")


class Settings(BaseSettings):
    """Class for project configurations."""

    telegram = Telegram()


settings = Settings()
