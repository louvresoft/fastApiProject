""" Vistas de user """
from typing import List, Union

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import User, ShowUser, UpdateUser
from app.db.database import get_db
from app.db import models

usuarios: List[User] = []

router = APIRouter(prefix="/user", tags=["Users"])


@router.get("/", response_model=List[ShowUser])
def obtener_usuarios(data_base: Session = Depends(get_db)) -> List[ShowUser]:
    """Metodo que retorna un listado de usuarios"""
    data = data_base.query(models.User).all()

    return data


@router.post("/")
def crear_usuario(user: User, data_base: Session = Depends(get_db)) -> dict[str, str]:
    """Crea un usuario"""
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
    data_base.add(nuevo_usuario)
    data_base.commit()
    data_base.refresh(nuevo_usuario)
    return {"respuesta": "Usuario creado correctamente!"}


@router.get("/{user_id}", response_model=ShowUser)
def obtener_usuario(user_id: int, data_base: Session = Depends(get_db)):
    """Obtiene un usuario por su id"""
    usuario = data_base.query(models.User).filter(models.User.id == user_id).first()
    if not usuario:
        return {"detail": "El usuario no existe"}
    return usuario


@router.delete("/")
def eliminar_usuario(
    user_id: int, data_base: Session = Depends(get_db)
) -> Union[dict[str, str], dict[str, str]]:
    """Elimina un usuario"""
    usuario = data_base.query(models.User).filter(models.User.id == user_id)
    if not usuario.first():
        return {"detail": "usuario no encontrado"}
    usuario.delete(synchronize_session=False)
    data_base.commit()
    return {"detail": "usuario eliminado correctamente."}


@router.patch("/{user_id}")
def actualizar_user(
    user_id: int, updateuser: UpdateUser, data_base: Session = Depends(get_db)
):
    """Actualiza un usuario"""
    usuario = data_base.query(models.User).filter(models.User.id == user_id)
    if not usuario.first():
        return {"detail": "Usuario no encontrado!!"}
    usuario.update(updateuser.dict(exclude_unset=True))
    data_base.commit()
    return {"detail": "Usuario actualizado correctamente."}
