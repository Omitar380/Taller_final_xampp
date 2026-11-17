import os

import mysql.connector
from mysql.connector import Error


def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            database=os.getenv("DB_NAME", "gestiona_cliente_db"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
        )
        if conexion.is_connected():
            print("¡Conexión exitosa a la base de datos!")
            return conexion
        conexion.close()
        print("No se pudo establecer la conexión con la base de datos.")
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    return None
