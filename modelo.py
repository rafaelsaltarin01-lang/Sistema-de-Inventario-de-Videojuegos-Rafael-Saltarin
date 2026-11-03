


class Producto:
    

    def __init__(self, nombre, precio, stock, id=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return (f"ID: {self.id} | Nombre: {self.nombre} | "
                f"Precio: ${self.precio:,.0f} | Stock: {self.stock}")
