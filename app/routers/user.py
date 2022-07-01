""" Vistas de user """
from typing import List, Union, Dict, Any

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from schemas import User, ShowUser, UpdateUser
from app.db.database import get_db
from app.repository import user

usuarios: List[User] = []

router = APIRouter(prefix="/user", tags=["Users"])


@router.get("/", response_model=List[ShowUser], status_code=status.HTTP_200_OK)
def obtener_usuarios(data_base: Session = Depends(get_db)) -> List[ShowUser]:
    """Metodo que retorna un listado de usuarios"""
    response = user.obtener_usuarios(data_base=data_base)
    return response


@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_usuario(usuario: User, data_base: Session = Depends(get_db)) -> dict[str, str]:
    """Crea un usuario"""
    user.crear_usuario(data_base=data_base, usuario=usuario)
    return {"respuesta": "Usuario creado correctamente!"}


@router.get("/{user_id}", response_model=ShowUser, status_code=status.HTTP_200_OK)
def obtener_usuario(user_id: int, data_base: Session = Depends(get_db)) -> object:
    """Obtiene un usuario por su id
    :param user_id: 
    :param data_base: 
    :return: 
    """
    usuario: Union[dict[str, str], Any] = user.obtener_usuario(user_id, data_base=data_base)
    return usuario


@router.delete("/", status_code=status.HTTP_200_OK)
def eliminar_usuario(
    user_id: int, data_base: Session = Depends(get_db)
) -> Union[dict[str, str], dict[str, str]]:
    """Elimina un usuario"""
    response = user.eliminar_usuario(user_id, data_base)
    return response


@router.patch("/{user_id}", status_code=status.HTTP_200_OK)
def actualizar_user(
    user_id: int, usuario_actualizado: UpdateUser, data_base: Session = Depends(get_db)
):
    """Actualiza un usuario"""
    usuario = user.actualizar_usuario(user_id, data_base=data_base, usuario_actualizado=usuario_actualizado)
    return usuario
