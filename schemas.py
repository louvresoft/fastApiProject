""" Schemas """
from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    """ User """
    username: str
    password: str
    nombre: str
    apellido: str
    direccion: Optional[str]
    telefono: int
    correo: str
    creacion: datetime = datetime.now()


class UserId(BaseModel):
    """User id"""

    id: int


class ShowUser(BaseModel):
    """Clase para de Response en un metodo"""

    username: str
    nombre: str
    correo: str

    class Config:
        """Bandera para declarar un base model como respomse"""

        orm_mode = True
