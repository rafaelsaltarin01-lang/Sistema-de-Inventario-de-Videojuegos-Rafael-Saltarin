

from base_datos import BaseDatos
from producto_dao import ProductoDAO
from producto_servicio import ProductoServicio

MENU = """
===== INVENTARIO DE VIDEOJUEGOS =====
1. Registrar videojuego
2. Mostrar inventario
3. Buscar videojuego
4. Actualizar videojuego
5. Eliminar videojuego
6. Vender unidades
7. Salir
"""


def pedir(texto):
    return input(texto).strip()


def registrar(servicio):
    nombre = pedir("Nombre: ")
    precio = pedir("Precio: ")
    stock = pedir("Cantidad disponible: ")
    producto = servicio.registrar(nombre, precio, stock)
    print(f"Videojuego guardado correctamente.\n{producto}")


def mostrar(servicio):
    productos = servicio.listar()
    if not productos:
        print("El inventario está vacío.")
        return
    for p in productos:
        print(p)


def buscar(servicio):
    print(servicio.buscar(pedir("ID del videojuego: ")))


def actualizar(servicio):
    id_producto = pedir("ID del videojuego a actualizar: ")
    actual = servicio.buscar(id_producto)
    print(f"Datos actuales: {actual}")
    nombre = pedir("Nuevo nombre: ")
    precio = pedir("Nuevo precio: ")
    stock = pedir("Nuevo stock: ")
    producto = servicio.actualizar(id_producto, nombre, precio, stock)
    print(f"Videojuego actualizado correctamente.\n{producto}")


def eliminar(servicio):
    producto = servicio.eliminar(pedir("ID del videojuego a eliminar: "))
    print(f"Se eliminó '{producto.nombre}' del inventario.")


def vender(servicio):
    id_producto = pedir("ID del videojuego: ")
    cantidad = pedir("Cantidad a vender: ")
    producto = servicio.vender(id_producto, cantidad)
    print(f"Venta realizada. Stock restante de '{producto.nombre}': {producto.stock}")


def main():
    base_datos = BaseDatos()
    base_datos.conectar()
    servicio = ProductoServicio(ProductoDAO(base_datos))

    acciones = {
        "1": registrar,
        "2": mostrar,
        "3": buscar,
        "4": actualizar,
        "5": eliminar,
        "6": vender,
    }

    try:
        while True:
            print(MENU)
            opcion = pedir("Elige una opción: ")
            if opcion == "7":
                print("Hasta pronto.")
                break
            accion = acciones.get(opcion)
            if accion is None:
                print("Opción no válida. Elige un número del 1 al 7.")
                continue
            try:
                accion(servicio)
            except ValueError as error:
                print(f"Error: {error}")
            except Exception as error:  
                print(f"Ocurrió un error inesperado: {error}")
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma finalizado.")
    finally:
        base_datos.cerrar()


if __name__ == "__main__":
    main()
