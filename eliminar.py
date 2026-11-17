from mysql.connector import Error


def eliminar_cliente(conexion, cliente_id):
    cursor = None
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = %s", (cliente_id,))
        conexion.commit()
        if cursor.rowcount:
            print(f"Cliente con ID {cliente_id} eliminado exitosamente.")
        else:
            print(f"No se encontró el cliente con ID {cliente_id}.")
    except Error as e:
        conexion.rollback()
        print(f"Error al eliminar el cliente: {e}")
    finally:
        if cursor is not None:
            cursor.close()