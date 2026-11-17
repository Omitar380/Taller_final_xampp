from conexion import conectar_bd
from consulta import consultar_clientes
from eliminar import eliminar_cliente
from insertar import insertar_cliente
from actualizar import actualizar_cliente


def pedir_id():
    while True:
        try:
            return int(input("ID del cliente: "))
        except ValueError:
            print("El ID debe ser un número entero.")


def pedir_datos_actualizar():
    opciones = {
        "1": ("nombre", "Nuevo nombre: "),
        "2": ("correo", "Nuevo correo: "),
        "3": ("telefono", "Nuevo teléfono: "),
    }
    campos = {}

    while True:
        print(
            "\n¿Qué dato quieres actualizar?\n"
            "1. Nombre\n"
            "2. Correo\n"
            "3. Teléfono\n"
            "4. Terminar selección"
        )
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "4":
            return campos
        if opcion not in opciones:
            print("Opción no válida.")
            continue

        campo, mensaje = opciones[opcion]
        valor = input(mensaje).strip()
        if valor:
            campos[campo] = valor
        else:
            print("El dato no puede quedar vacío.")


def main():
    conexion = conectar_bd()
    if conexion is None:
        return

    try:
        while True:
            print(
                "\n--- Gestión de clientes ---\n"
                "1. Registrar cliente\n"
                "2. Consultar clientes\n"
                "3. Actualizar cliente\n"
                "4. Eliminar cliente\n"
                "5. Salir"
            )
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                nombre = input("Nombre: ").strip()
                correo = input("Correo: ").strip()
                telefono = input("Teléfono: ").strip()
                if nombre and correo and telefono:
                    insertar_cliente(conexion, nombre, correo, telefono)
                else:
                    print("Todos los campos son obligatorios.")
            elif opcion == "2":
                consultar_clientes(conexion)
            elif opcion == "3":
                cliente_id = pedir_id()
                campos = pedir_datos_actualizar()
                actualizar_cliente(conexion, cliente_id, campos)
            elif opcion == "4":
                cliente_id = pedir_id()
                confirmacion = input(
                    f"¿Eliminar el cliente {cliente_id}? (s/N): "
                ).strip().lower()
                if confirmacion == "s":
                    eliminar_cliente(conexion, cliente_id)
            elif opcion == "5":
                break
            else:
                print("Opción no válida.")
    finally:
        conexion.close()


if __name__ == "__main__":
    main()
