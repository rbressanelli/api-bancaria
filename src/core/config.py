from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "API Bancaria"
    APP_VERSION: str = "0.1.0"
    APP_DESCRIPTION: str = "API bancaria assincrona com FastAPI"
    SECRET_KEY: str = "troque-esta-chave-por-uma-chave-segura"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    DATABASE_URL: str = "sqlite+aiosqlite:///./bank.db"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
