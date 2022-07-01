from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi import HTTPException, status
from app.db import models
from app.hashing import Hash

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def crear_usuario(usuario, data_base: Session):
    usuario = usuario.dict()
    try:
        nuevo_usuario = models.User(
            username=usuario.get("username"),
            password=Hash.hash_password(usuario.get("password")),
            nombre=usuario.get("nombre"),
            apellido=usuario.get("apellido"),
            direccion=usuario.get("direccion"),
            telefono=usuario.get("telefono"),
            correo=usuario.get("correo"),
        )
        data_base.add(nuevo_usuario)
        data_base.commit()
        data_base.refresh(nuevo_usuario)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Error creando usuario {e}"
        )


def obtener_usuario(user_id, data_base: Session):
    usuario = data_base.query(models.User).filter(models.User.id == user_id).first()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"no existe el usuario con el id {user_id}"
        )
    return usuario


def eliminar_usuario(user_id, data_base: Session):
    usuario = data_base.query(models.User).filter(models.User.id == user_id)
    if not usuario.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe el usuario con el id {user_id} por lo tanto no es posible eliminarlo"
        )
    usuario.delete(synchronize_session=False)
    data_base.commit()
    return {"detail": "usuario eliminado correctamente."}


def obtener_usuarios(data_base: Session):
    data = data_base.query(models.User).all()
    return data


def actualizar_usuario(usuario_id, data_base: Session, usuario_actualizado):
    usuario = data_base.query(models.User).filter(models.User.id == usuario_id)
    if not usuario.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe el usuario con el id {usuario_id}"
        )
    usuario.update(usuario_actualizado.dict(exclude_unset=True))
    data_base.commit()
    return {"detail": "Usuario actualizado correctamente."}
