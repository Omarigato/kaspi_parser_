from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Kaspi Parser"
    db_host: str = "db"
    db_port: int = 5432
    db_user: str = "postgres"
    db_password: str = "postgres"
    db_name: str = "kaspi"
    db_url: str = f"postgresql+psycopg2://postgres:postgres@db:5432/kaspi"

    class Config:
        env_file = ".env"

settings = Settings()
