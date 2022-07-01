""" Congiguracion de variables de entorno """
import os
from typing import Optional
from pathlib import Path

from dotenv import load_dotenv


env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    """Clase de configuracion de settings"""

    PROJECT_NAME: str = "PROYECTO-FAST-API"
    PROJECT_VERSION: str = "1.0"
    POSTGRES_USER: Optional[str] = os.getenv("POSTGRES_USER")
    POSTGRES_DB: Optional[str] = os.getenv("POSTGRES_DB")
    POSTGRES_PASSWORD: Optional[str] = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST: Optional[str] = os.getenv("POSTGRES_HOST")
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Pruebas12345*@localhost/fastapi"
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"


settings = Settings()
