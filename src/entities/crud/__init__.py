from .crud_usuario import (
    crear_usuario,
    listar_usuarios,
    editar_usuario,
    eliminar_usuario,
)
from .crud_cliente import (
    crear_cliente,
    listar_clientes,
    editar_cliente,
    eliminar_cliente,
)
from .crud_empleado import (
    crear_empleado,
    listar_empleados,
    editar_empleado,
    eliminar_empleado,
)
from .crud_vehiculo import (
    crear_vehiculo,
    listar_vehiculos,
    editar_vehiculo,
    eliminar_vehiculo,
)
from .crud_metodo_pago import (
    crear_metodo_pago,
    listar_metodos_pago,
    editar_metodo_pago,
    eliminar_metodo_pago,
)
from .crud_mantenimiento import (
    crear_mantenimiento,
    listar_mantenimientos,
    editar_mantenimiento,
    eliminar_mantenimiento,
)
from .crud_venta import crear_venta, listar_ventas, editar_venta, eliminar_venta

__all__ = [
    # Usuario
    "crear_usuario",
    "listar_usuarios",
    "editar_usuario",
    "eliminar_usuario",
    # Cliente
    "crear_cliente",
    "listar_clientes",
    "editar_cliente",
    "eliminar_cliente",
    # Empleado
    "crear_empleado",
    "listar_empleados",
    "editar_empleado",
    "eliminar_empleado",
    # Vehiculo
    "crear_vehiculo",
    "listar_vehiculos",
    "editar_vehiculo",
    "eliminar_vehiculo",
    # MetodoPago
    "crear_metodo_pago",
    "listar_metodos_pago",
    "editar_metodo_pago",
    "eliminar_metodo_pago",
    # Mantenimiento
    "crear_mantenimiento",
    "listar_mantenimientos",
    "editar_mantenimiento",
    "eliminar_mantenimiento",
    # Venta
    "crear_venta",
    "listar_ventas",
    "editar_venta",
    "eliminar_venta",
]
