from mysql.connector import Error


def consultar_clientes(conexion):
    cursor = None
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, nombre, correo, telefono FROM clientes ORDER BY id"
        )
        resultados = cursor.fetchall()

        if not resultados:
            print("No hay clientes registrados.")
            return

        for cliente in resultados:
            print(
                f"ID: {cliente[0]} | Nombre: {cliente[1]} | "
                f"Correo: {cliente[2]} | Teléfono: {cliente[3]}"
            )
    except Error as e:
        print(f"Error al consultar clientes: {e}")
    finally:
        if cursor is not None:
            cursor.close()