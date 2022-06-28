import  psycopg2


connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="Pruebas12345*",
    database="fastapi"
)

connection.autocommit = True


def crearTabla():
    cursor = connection.cursor()
    query = "CREATE TABLE usuario(nombre varchar(30), correo varchar(30), telefono varchar(30))"
    try:
        cursor.execute(query)
    except:
        print("la tabal usuario ya existe")
    cursor.close()


def insertarDatos():
    cursor = connection.cursor()
    query = f""" INSERT INTO usuario (nombre, correo, telefono) values ('andres', 'andres@gmail.com', '239034304' ) """

    try:
        cursor.execute(query)
    except:
        print("Errores al insertar datos")


def eliminarTabla():
    cursor = connection.cursor()
    query = "DROP TABLE usuario"
    cursor.execute(query)
    cursor.close()

crearTabla()
insertarDatos()
#eliminarTabla()