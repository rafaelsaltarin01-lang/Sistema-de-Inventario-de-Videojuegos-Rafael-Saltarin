

from modelo import Producto


class ProductoServicio:
    def __init__(self, dao):
        self.dao = dao

    # Validaciones 
    @staticmethod
    def _validar_nombre(nombre):
        if nombre is None or not str(nombre).strip():
            raise ValueError("El nombre no puede estar vacío.")
        return str(nombre).strip()

    @staticmethod
    def _validar_precio(precio):
        try:
            precio = float(precio)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser un número.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        return precio

    @staticmethod
    def _validar_stock(stock):
        try:
            if isinstance(stock, float) and not stock.is_integer():
                raise ValueError
            stock = int(stock)
        except (TypeError, ValueError):
            raise ValueError("El stock debe ser un número entero.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        return stock

    @staticmethod
    def _validar_id(id_producto):
        try:
            return int(id_producto)
        except (TypeError, ValueError):
            raise ValueError("El ID debe ser un número entero.")

    def _obtener_existente(self, id_producto):
        id_producto = self._validar_id(id_producto)
        producto = self.dao.buscar_por_id(id_producto)
        if producto is None:
            raise ValueError(f"No existe un videojuego con ID {id_producto}.")
        return producto

    #  Operaciones 
    def registrar(self, nombre, precio, stock):
        producto = Producto(
            self._validar_nombre(nombre),
            self._validar_precio(precio),
            self._validar_stock(stock),
        )
        return self.dao.insertar(producto)

    def listar(self):
        return self.dao.listar()

    def buscar(self, id_producto):
        return self._obtener_existente(id_producto)

    def actualizar(self, id_producto, nombre, precio, stock):
        producto = self._obtener_existente(id_producto)
        producto.nombre = self._validar_nombre(nombre)
        producto.precio = self._validar_precio(precio)
        producto.stock = self._validar_stock(stock)
        self.dao.actualizar(producto)
        return producto

    def eliminar(self, id_producto):
        producto = self._obtener_existente(id_producto)
        self.dao.eliminar(producto.id)
        return producto

    def vender(self, id_producto, cantidad):
        producto = self._obtener_existente(id_producto)
        try:
            cantidad = int(cantidad)
        except (TypeError, ValueError):
            raise ValueError("La cantidad a vender debe ser un número entero.")
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor que cero.")
        if cantidad > producto.stock:
            raise ValueError(
                f"Stock insuficiente: solo hay {producto.stock} unidades disponibles."
            )
        producto.stock -= cantidad
        self.dao.actualizar_stock(producto.id, producto.stock)
        return producto
