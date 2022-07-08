import logging
import random
import sys
import os

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from main import app
from app.db.models import Base
from app.hashing import Hash
from app.db.database import get_db


db_path = os.path.join(os.path.dirname(__file__), "test.db")
db_url = "sqlite:///{}".format(db_path)
SQLALCHEMY_DATABASE_RUL = db_url
engine_test = create_engine(
    SQLALCHEMY_DATABASE_RUL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(bind=engine_test, autocommit=False, autoflush=False)
Base.metadata.create_all(bind=engine_test)


cliente = TestClient(app)


def insertar_usuario_prueba():
    password_hash = Hash.hash_password("prueba12")
    random_number = random.randint(1, 1000)
    engine_test.execute(
        f"""
        INSERT INTO usuario(username,password,nombre,apellido,direccion,telefono,correo)
        values
        ('prueba','{password_hash}','prueba_nombre','prueba_apellido','prueba_direccion',1212,'prueba_{random_number}@gmail.com')
        """
    )


insertar_usuario_prueba()


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


def test_crear_usuario():
    usuario_datos = {
        "username": "dafma1",
        "password": "Pruebas123*1",
        "nombre": "Dafma1",
        "apellido": "Reads1",
        "direccion": "Toluca1",
        "telefono": 1234561,
        "correo": "dafma1@gmail.com",
        "creacion": "2022-07-04T21:21:59.979195",
    }

    usuario = {
        "username": "prueba",
        "password": "prueba12"
    }
    response_token = cliente.post('/login/', data=usuario)
    assert response_token.status_code == 200
    assert response_token.json()["token_type"] == "bearer"

    headers = {
        "Authorization": f"Bearer {response_token.json()['access_token']}"
    }

    response = cliente.post('/user/', json=usuario_datos, headers=headers)
    assert response.status_code == 201
    assert response.json()["respuesta"] == "Usuario creado correctamente!"


def test_delete_database():
    db_path = os.path.join(os.path.dirname(__file__), "test.db")
    os.remove(db_path)
