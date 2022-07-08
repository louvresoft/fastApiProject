# Crear migraciones con alembic
-> Crea las migraciones
alembic revision --autogenerate -m ".\crear modelos v2"
-> Crea los modelos
alembic upgrade heads 


# Correr el coverage
coverage run -m pytest
# Generar reporte
coverage html
