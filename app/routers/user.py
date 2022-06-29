import logging
from typing import List, Union

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import User, ShowUser
from app.db.database import get_db
from app.db import models

usuarios: List[User] = []

router = APIRouter(prefix="/user", tags=["Users"])


@router.get("/")
def obtener_usuarios(db: Session = Depends(get_db), response_model=List[ShowUser]) -> List[User]:
    """ Metodo que retorna un listado de usuarios"""
    data = db.query(models.User).all()
    logging.debug(data)

    return data


@router.post("/")
def crear_usuario(user: User, db: Session = Depends(get_db)) -> dict[str, str]:
    usuario = user.dict()

    nuevo_usuario = models.User(
        username=usuario.get("username"),
        password=usuario.get("password"),
        nombre=usuario.get("nombre"),
        apellido=usuario.get("apellido"),
        direccion=usuario.get("direccion"),
        telefono=usuario.get("telefono"),
        correo=usuario.get("correo"),
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return {"respuesta": "Usuario creado correctamente!"}


@router.get("/{user_id}", response_model=ShowUser)
def obtener_usuario(user_id: int, db: Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id == user_id).first()
    if not usuario:
        return {"detail": "El usuario no existe"}
    return usuario


@router.delete("/")
def eliminar_usuario(user_id: int) -> Union[dict[str, str], dict[str, str]]:
    for index, user in enumerate(usuarios):
        if user["id"] == user_id:
            usuarios.pop(index)
            return {"respuesta": "Usuario eliminado correctamente"}
    return {"respuesta": "usuario no encontrado!!"}


@router.put("/{user_id}")
def actualizar_user(user_id: int, updateuser: User):
    for index, user in enumerate(usuarios):
        if user["id"] == user_id:
            usuarios[index]["title"] = updateuser.dict()["title"]
            usuarios[index]["content"] = updateuser.dict()["content"]
            usuarios[index]["author"] = updateuser.dict()["author"]
            return {"respuesta": "Usuario actualizado correctamente!!"}
    return {"respuesta": "Usuario no encontrado!!"}
