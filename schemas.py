""" Schemas """
from typing import Optional, Union
from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    """User"""

    username: str
    password: str
    nombre: str
    apellido: str
    direccion: Optional[str]
    telefono: int
    correo: str
    creacion: datetime = datetime.now()


class UpdateUser(BaseModel):
    """User"""

    username: str
    password: str
    nombre: str
    apellido: str
    direccion: str
    telefono: int
    correo: str
    creacion: datetime


class UserId(BaseModel):
    """User id"""

    id: int


class ShowUser(BaseModel):
    """Clase para de Response en un metodo"""

    username: str
    nombre: str
    correo: str

    class Config:

        """ Bandera para declarar un base model como response """

        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    usernem: Union[str, None] = None
