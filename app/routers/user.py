import logging
from typing import List, Union

from fastapi import APIRouter, Depends

from schemas import User, UserId
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models

usuarios: List[User] = []

router = APIRouter(prefix="/user", tags=["Users"])


@router.get("/")
def obtener_usuarios(db: Session = Depends(get_db)) -> List[User]:
    """ metodo que retorna un listado de usuarios """
    data = db.query(models.User).all()
    logging.info("aqui todo bien")
    logging.debug(data)

    return usuarios


@router.post("/ruta2")
def ruta2(user: User) -> dict[str, str]:
    usuario = user.dict()
    usuarios.append(usuario)
    return {"respuesta": "Usuario creado satisfactoriamente!"}


@router.post("/{user_id}")
def obtener_usuario(user_id: int):
    for user in usuarios:
        if user["id"] == user_id:
            return {"usuario": user["id"]}
    return {"detail": "Usuario no exoste"}


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
