import logging
from datetime import timedelta

from sqlalchemy.orm import Session
from app.db import models
from fastapi import HTTPException, status
from app.hashing import Hash
from app.token import create_access_token


def auth_user(usuario, db: Session):
    user = (
        db.query(models.User)
        .filter(models.User.username == usuario.username)
        .first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe el usuario  {usuario.username} por lo tanto no es posible loguearse",
        )
    if not Hash.verify_password(usuario.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Password incorrecto",
        )
    access_token = create_access_token(
        data={"sub": user.username}
    )
    return {"access_token": access_token, "token_type" : "bearer"}
