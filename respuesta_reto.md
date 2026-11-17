# Reto 12: sistema de gestión de clientes

## A. Crear la base de datos y la tabla

1. Instalar Python y ejecutar `pip install mysql-connector-python`.
2. Abrir el panel de XAMPP e iniciar el servicio **MySQL** (o MariaDB).
3. Abrir phpMyAdmin desde XAMPP.
4. Importar el archivo `gestion_clientes.sql`. Este crea la base `gestiona_cliente_db` y la tabla `clientes`.
5. Ejecutar el programa con `python main.py`.

## B. Conexión entre Python y la base de datos

Se instala el conector oficial con `pip install mysql-connector-python` y se importa `mysql.connector`. La función `conectar_bd()` de `conexion.py` conecta con el servidor local de XAMPP, selecciona `gestiona_cliente_db` y devuelve la conexión para que las otras funciones la utilicen. Si ocurre un error, informa del problema y devuelve `None`.

La configuración local predeterminada usa `root` sin contraseña, que es común en una instalación local de XAMPP. Para cambiarla, se pueden definir las variables de entorno `DB_HOST`, `DB_NAME`, `DB_USER` y `DB_PASSWORD`. No se debe usar una cuenta `root` sin contraseña en un servidor expuesto o de producción.

## C. SQL para crear la tabla

```sql
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(150) NOT NULL UNIQUE,
    telefono VARCHAR(25) NOT NULL
);
```

El esquema completo, incluida la creación de la base de datos, está en `gestion_clientes.sql`.

## D. Consulta de todos los clientes

```sql
SELECT id, nombre, correo, telefono
FROM clientes
ORDER BY id;
```

La función `consultar_clientes()` ejecuta esta consulta y muestra los resultados.

## E. Actualización y eliminación desde Python

`actualizar_cliente()` ejecuta un `UPDATE` y `eliminar_cliente()` un `DELETE`. Al actualizar, el menú permite elegir uno o más campos (nombre, correo o teléfono), por lo que los demás datos del cliente permanecen sin cambios. Los valores se pasan mediante parámetros `%s` en lugar de concatenarlos en el SQL. Las funciones confirman los cambios con `commit()` y hacen `rollback()` si MySQL devuelve un error. El archivo `main.py` ofrece un menú para registrar, consultar, actualizar y eliminar clientes.

## F. Medidas de seguridad

- Usar consultas parametrizadas para impedir inyección SQL.
- Validar que los campos obligatorios estén completos y que el identificador sea numérico.
- Crear para la aplicación un usuario MySQL propio con permisos mínimos; no usar `root` ni una contraseña vacía fuera del entorno local.
- Guardar credenciales en variables de entorno y no en el código ni en repositorios.
- Restringir el acceso al servidor y a phpMyAdmin, y mantener copias de seguridad de la base de datos.
- Confirmar las eliminaciones antes de ejecutarlas y manejar errores sin mostrar credenciales.
