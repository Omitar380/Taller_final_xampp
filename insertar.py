from mysql.connector import Error


def insertar_cliente(conexion, nombre, correo, telefono):
    cursor = None
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO clientes (nombre, correo, telefono) "
            "VALUES (%s, %s, %s)",
            (nombre, correo, telefono),
        )
        conexion.commit()
        print(f"Cliente registrado con ID {cursor.lastrowid}.")
    except Error as e:
        conexion.rollback()
        print(f"Error al registrar el cliente: {e}")
    finally:
        if cursor is not None:
            cursor.close()
