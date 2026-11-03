# Sistema de Inventario de Videojuegos

Aplicación de consola en Python que administra un inventario de videojuegos con SQLite, aplicando el patrón **DAO** y separación de responsabilidades. Permite registrar, listar, buscar, actualizar y eliminar videojuegos, además de vender unidades descontándolas del stock. Los datos se conservan entre ejecuciones en el archivo `inventario.db`.

## Estructura

| Archivo | Responsabilidad |
|---|---|
| `modelo.py` | Clase `Producto` (id, nombre, precio, stock). |
| `base_datos.py` | Clase `BaseDatos`: conexión a SQLite y creación de la tabla `productos`. |
| `producto_dao.py` | Clase `ProductoDAO`: todas las consultas SQL (insertar, listar, buscar, actualizar, eliminar). |
| `producto_servicio.py` | Clase `ProductoServicio`: validaciones y reglas de negocio. |
| `main.py` | Menú interactivo. No contiene SQL; solo usa el servicio. |
| `pruebas.py` | Script que ejecuta los casos de prueba con una base temporal. |

## Funcionalidades

1. Registrar videojuego (nombre, precio, cantidad).
2. Mostrar inventario (ID, nombre, precio, stock).
3. Buscar videojuego por ID (informa si no existe).
4. Actualizar nombre, precio y stock.
5. Eliminar videojuego por ID.
6. Vender unidades (descuenta del stock).
7. Salir.

## Validaciones

- Nombre no vacío.
- Precio mayor que cero.
- Stock no negativo.
- Venta con cantidad mayor que cero y no superior al stock disponible.
- Aviso cuando el ID no existe.
- Entradas inválidas (texto en lugar de números, etc.) muestran un mensaje y no cierran el programa.

## Cómo ejecutarlo

Requiere Python 3.8+ (solo biblioteca estándar, sin instalar nada).

```bash
python main.py     
```

La base `inventario.db` se crea automáticamente la primera vez.

## Evidencias de pruebas

Salida real de `python pruebas.py`:

| Prueba | Resultado |
|---|---|
| Registrar Resident Evil 4 (180000, stock 10) | OK: `ID: 1 \| Resident Evil 4 \| $180,000 \| Stock: 10` |
| Mostrar inventario | OK: aparecen los productos registrados |
| Buscar ID existente | OK: se muestran los datos del producto |
| Buscar ID inexistente (19) | RECHAZADO: `No existe un videojuego con ID 999.` |
| Actualizar Elden Ring | OK: cambios verificados con una nueva conexión a SQLite |
| Vender 3 unidades de Resident Evil 4 | OK: stock 10 → 7 |
| Vender 20 unidades | RECHAZADO: `Stock insuficiente: solo hay 7 unidades disponibles.` (stock sigue en 7) |
| Vender 0 unidades | RECHAZADO: `La cantidad a vender debe ser mayor que cero.` |
| Nombre vacío / precio 0 / stock negativo | RECHAZADO con su mensaje correspondiente |
| Eliminar un producto | OK: deja de aparecer en el inventario |
