import pathlib

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    JWT_SECRET: str
    JWT_ALGORITHM: str

    APP_NAME: str
    APP_URL: str

    DB_HOST: str
    DB_PORT: int
    DB_DATABASE: str
    DB_USER: str
    DB_PASSWORD: str

    STEAM_WEBAPI_KEY: str
    STEAM_COOKIE: str

    class Config:
        env_file = f"{pathlib.Path(__file__).resolve().parent}/.env"

    def db_url(self) -> str:
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_DATABASE}"


settings = Settings()
