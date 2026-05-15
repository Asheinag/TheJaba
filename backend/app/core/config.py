from functools import lru_cache

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",  # игнорировать неизвестные переменные в .env
    )

    database_url: PostgresDsn

    # App
    app_name: str = "The Jaba"
    debug: bool = False

    # CORS
    allowed_origins_list: list[str] = ["http://localhost:5173"]

# Чтение и разбор файла - недешево, делаем кэширование чтобы обращаться к сеттингам один раз
@lru_cache
def get_settings() -> Settings:
    return Settings()
