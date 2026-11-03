

import sqlite3


class BaseDatos:
    def __init__(self, ruta="inventario.db"):
        self.ruta = ruta
        self.conexion = None

    def conectar(self):
        if self.conexion is None:
            self.conexion = sqlite3.connect(self.ruta)
            self.crear_tabla()
        return self.conexion

    def crear_tabla(self):
        self.conexion.execute(
            """
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL,
                stock INTEGER NOT NULL
            )
            """
        )
        self.conexion.commit()

    def cerrar(self):
        if self.conexion is not None:
            self.conexion.close()
            self.conexion = None
