from sqlalchemy.orm import Session

from app.db import models


def crear_usuario(usuario, data_base: Session):
    usuario = usuario.dict()
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


def obtener_usuario(user_id, data_base: Session):
    usuario = data_base.query(models.User).filter(models.User.id == user_id).first()
    if not usuario:
        return {"detail": "El usuario no existe"}
    return usuario


def eliminar_usuario(user_id, data_base: Session):
    usuario = data_base.query(models.User).filter(models.User.id == user_id)
    if not usuario.first():
        return {"detail": "usuario no encontrado"}
    usuario.delete(synchronize_session=False)
    data_base.commit()
    return {"detail": "usuario eliminado correctamente."}


def obtener_usuarios(data_base: Session):
    data = data_base.query(models.User).all()
    return data


def actualizar_usuario(usuario_id, data_base: Session, usuario_actualizado):
    usuario = data_base.query(models.User).filter(models.User.id == usuario_id)
    if not usuario.first():
        return {"detail": "Usuario no encontrado!!"}
    usuario.update(usuario_actualizado.dict(exclude_unset=True))
    data_base.commit()
    return {"detail": "Usuario actualizado correctamente."}
