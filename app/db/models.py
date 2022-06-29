""" Modelos para la aplicacion """
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.db.database import Base


class User(Base):
    """ Modelo Usuario"""
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    apellido = Column(String)
    direccion = Column(String)
    telefono = Column(Integer)
    correo = Column(String)
    creacion = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    estado = Column(Boolean)
