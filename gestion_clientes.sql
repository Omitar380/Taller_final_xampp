CREATE DATABASE IF NOT EXISTS gestiona_cliente_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE gestiona_cliente_db;

CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(150) NOT NULL UNIQUE,
    telefono VARCHAR(25) NOT NULL
);
