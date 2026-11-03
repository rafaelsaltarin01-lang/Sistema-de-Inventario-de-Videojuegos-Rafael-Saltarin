

from modelo import Producto


class ProductoDAO:
    def __init__(self, base_datos):
        self.base_datos = base_datos

    def _con(self):
        return self.base_datos.conectar()

    @staticmethod
    def _a_producto(fila):
        return Producto(id=fila[0], nombre=fila[1], precio=fila[2], stock=fila[3])

    def insertar(self, producto):
        con = self._con()
        cursor = con.execute(
            "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
            (producto.nombre, producto.precio, producto.stock),
        )
        con.commit()
        producto.id = cursor.lastrowid
        return producto

    def listar(self):
        filas = self._con().execute(
            "SELECT id, nombre, precio, stock FROM productos ORDER BY id"
        ).fetchall()
        return [self._a_producto(f) for f in filas]

    def buscar_por_id(self, id_producto):
        fila = self._con().execute(
            "SELECT id, nombre, precio, stock FROM productos WHERE id = ?",
            (id_producto,),
        ).fetchone()
        return self._a_producto(fila) if fila else None

    def actualizar(self, producto):
        con = self._con()
        cursor = con.execute(
            "UPDATE productos SET nombre = ?, precio = ?, stock = ? WHERE id = ?",
            (producto.nombre, producto.precio, producto.stock, producto.id),
        )
        con.commit()
        return cursor.rowcount > 0

    def actualizar_stock(self, id_producto, nuevo_stock):
        con = self._con()
        cursor = con.execute(
            "UPDATE productos SET stock = ? WHERE id = ?",
            (nuevo_stock, id_producto),
        )
        con.commit()
        return cursor.rowcount > 0

    def eliminar(self, id_producto):
        con = self._con()
        cursor = con.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        con.commit()
        return cursor.rowcount > 0
