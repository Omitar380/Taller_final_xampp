from mysql.connector import Error


def actualizar_cliente(conexion, cliente_id, campos):
    columnas_permitidas = {"nombre", "correo", "telefono"}
    campos_actualizar = {
        campo: valor
        for campo, valor in campos.items()
        if campo in columnas_permitidas and valor
    }
    if not campos_actualizar:
        print("No se seleccionaron datos para actualizar.")
        return

    cursor = None
    try:
        cursor = conexion.cursor()
        columnas_sql = ", ".join(
            f"{campo} = %s" for campo in campos_actualizar
        )
        sql = f"UPDATE clientes SET {columnas_sql} WHERE id = %s"
        valores = (*campos_actualizar.values(), cliente_id)
        cursor.execute(sql, valores)
        conexion.commit()
        if cursor.rowcount:
            print(f"Cliente con ID {cliente_id} actualizado exitosamente.")
        else:
            print(
                f"No hubo cambios para el cliente con ID {cliente_id}; "
                "puede que no exista o que ya tuviera esos datos."
            )
    except Error as e:
        conexion.rollback()
        print(f"Error al actualizar: {e}")
    finally:
        if cursor is not None:
            cursor.close()