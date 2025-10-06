import os

class Settings:
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://kaspi:kaspi@localhost:5432/kaspi"
    )

settings = Settings()
