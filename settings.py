from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    JWT_SECRET: str
    JWT_ALGORITHM: str

    APP_NAME: str
    APP_URL: str

    MARIADB_HOST: str
    MARIADB_PORT: int
    MARIADB_DATABASE: str
    MARIADB_USER: str
    MARIADB_PASSWORD: str
    MARIADB_ROOT_PASSWORD: str

    STEAM_WEBAPI_KEY: str
    STEAM_COOKIE: str

    class Config:
        env_file = ".env"

    def db_url(self) -> str:
        if self.MARIADB_USER == "root":
            return f"mysql+pymysql://{self.MARIADB_USER}:{self.MARIADB_ROOT_PASSWORD}@{self.MARIADB_HOST}:{self.MARIADB_PORT}/{self.MARIADB_DATABASE}"
        return f"mysql+pymysql://{self.MARIADB_USER}:{self.MARIADB_PASSWORD}@{self.MARIADB_HOST}:{self.MARIADB_PORT}/{self.MARIADB_DATABASE}"


settings = Settings()

