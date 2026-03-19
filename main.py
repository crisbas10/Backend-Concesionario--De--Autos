from datetime import datetime
from src.entities import (
    Base,
    Usuario,
    Cliente,
    Empleado,
    Vehiculo,
    MetodoPago,
    Mantenimiento,
    Venta,
)
from src.entities.databases.conexion import engine, get_session
from src.entities.crud import (
    crear_usuario,
    listar_usuarios,
    editar_usuario,
    eliminar_usuario,
    crear_cliente,
    listar_clientes,
    editar_cliente,
    eliminar_cliente,
    crear_empleado,
    listar_empleados,
    editar_empleado,
    eliminar_empleado,
    crear_vehiculo,
    listar_vehiculos,
    editar_vehiculo,
    eliminar_vehiculo,
    crear_metodo_pago,
    listar_metodos_pago,
    editar_metodo_pago,
    eliminar_metodo_pago,
    crear_mantenimiento,
    listar_mantenimientos,
    editar_mantenimiento,
    eliminar_mantenimiento,
    crear_venta,
    listar_ventas,
    editar_venta,
    eliminar_venta,
)

# Crear todas las tablas en Neon al iniciar
Base.metadata.create_all(bind=engine)
print(" Tablas sincronizadas con Neon correctamente\n")


def menu_principal():
    print("\n" + "=" * 50)
    print("     CONCESIONARIO DE AUTOS - SISTEMA ORM  ")
    print("=" * 50)
    print("  1. Usuarios")
    print("  2. Clientes")
    print("  3. Empleados")
    print("  4. Vehículos")
    print("  5. Métodos de Pago")
    print("  6. Mantenimientos")
    print("  7. Ventas")
    print("  0. Salir")
    print("=" * 50)
    return input("Selecciona una opción: ").strip()


def menu_crud(entidad: str):
    print(f"\n--- {entidad.upper()} ---")
    print("  1. Crear")
    print("  2. Listar")
    print("  3. Editar")
    print("  4. Eliminar")
    print("  0. Volver")
    return input("Selecciona una opción: ").strip()


def flujo_usuario(session):
    while True:
        op = menu_crud("Usuarios")
        if op == "1":
            nombre = input("Nombre de usuario: ")
            correo = input("Correo: ")
            password = input("Password: ")
            rol = input("Rol (vendedor/admin) [vendedor]: ") or "vendedor"
            crear_usuario(session, nombre, correo, password, rol)
        elif op == "2":
            listar_usuarios(session)
        elif op == "3":
            listar_usuarios(session)
            uid = int(input("ID del usuario a editar: "))
            nombre = input("Nuevo nombre (vacío para no cambiar): ").strip()
            correo = input("Nuevo correo: ").strip()
            rol = input("Nuevo rol: ").strip()
            cambios = {}
            if nombre:
                cambios["nombre_usuario"] = nombre
            if correo:
                cambios["correo"] = correo
            if rol:
                cambios["rol"] = rol
            editar_usuario(session, uid, **cambios)
        elif op == "4":
            listar_usuarios(session)
            uid = int(input("ID del usuario a eliminar: "))
            if input(f"¿Seguro? (s/n): ").lower() == "s":
                eliminar_usuario(session, uid)
        elif op == "0":
            break


def flujo_cliente(session):
    while True:
        op = menu_crud("Clientes")
        if op == "1":
            listar_usuarios(session)
            uid = int(input("ID del usuario que crea: "))
            nombre = input("Nombre del cliente: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            crear_cliente(session, nombre, telefono, correo, uid)
        elif op == "2":
            listar_clientes(session)
        elif op == "3":
            listar_clientes(session)
            cid = int(input("ID del cliente a editar: "))
            listar_usuarios(session)
            uid = int(input("ID del usuario que edita: "))
            nombre = input("Nuevo nombre: ").strip()
            telefono = input("Nuevo teléfono: ").strip()
            correo = input("Nuevo correo: ").strip()
            cambios = {}
            if nombre:
                cambios["nombre"] = nombre
            if telefono:
                cambios["telefono"] = telefono
            if correo:
                cambios["correo"] = correo
            editar_cliente(session, cid, uid, **cambios)
        elif op == "4":
            listar_clientes(session)
            cid = int(input("ID del cliente a eliminar: "))
            if input("¿Seguro? (s/n): ").lower() == "s":
                eliminar_cliente(session, cid)
        elif op == "0":
            break


def flujo_empleado(session):
    while True:
        op = menu_crud("Empleados")
        if op == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            salario = float(input("Salario: "))
            cargo = input("Cargo: ")
            crear_empleado(session, nombre, telefono, correo, salario, cargo)
        elif op == "2":
            listar_empleados(session)
        elif op == "3":
            listar_empleados(session)
            eid = int(input("ID del empleado a editar: "))
            nombre = input("Nuevo nombre: ").strip()
            cargo = input("Nuevo cargo: ").strip()
            salario = input("Nuevo salario: ").strip()
            cambios = {}
            if nombre:
                cambios["nombre"] = nombre
            if cargo:
                cambios["cargo"] = cargo
            if salario:
                cambios["salario"] = float(salario)
            editar_empleado(session, eid, **cambios)
        elif op == "4":
            listar_empleados(session)
            eid = int(input("ID del empleado a eliminar: "))
            if input("¿Seguro? (s/n): ").lower() == "s":
                eliminar_empleado(session, eid)
        elif op == "0":
            break


def flujo_vehiculo(session):
    while True:
        op = menu_crud("Vehículos")
        if op == "1":
            listar_usuarios(session)
            uid = int(input("ID del usuario que registra: "))
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            anio = int(input("Año: "))
            precio = float(input("Precio: "))
            kilometraje = int(input("Kilometraje: "))
            estado = input("Estado (nuevo/usado): ")
            disp = input("¿Disponible? (s/n): ").lower() == "s"
            crear_vehiculo(
                session, marca, modelo, anio, precio, kilometraje, estado, disp, uid
            )
        elif op == "2":
            listar_vehiculos(session)
        elif op == "3":
            listar_vehiculos(session)
            vid = int(input("ID del vehículo a editar: "))
            listar_usuarios(session)
            uid = int(input("ID del usuario que edita: "))
            precio = input("Nuevo precio (vacío para no cambiar): ").strip()
            estado = input("Nuevo estado: ").strip()
            disp = input("¿Disponible? (s/n/vacío): ").strip()
            cambios = {}
            if precio:
                cambios["precio"] = float(precio)
            if estado:
                cambios["estado"] = estado
            if disp:
                cambios["disponibilidad"] = disp.lower() == "s"
            editar_vehiculo(session, vid, uid, **cambios)
        elif op == "4":
            listar_vehiculos(session)
            vid = int(input("ID del vehículo a eliminar: "))
            if input("¿Seguro? (s/n): ").lower() == "s":
                eliminar_vehiculo(session, vid)
        elif op == "0":
            break


def flujo_metodo_pago(session):
    while True:
        op = menu_crud("Métodos de Pago")
        if op == "1":
            tipo = input("Tipo (Efectivo/Crédito/Débito/Transferencia): ")
            crear_metodo_pago(session, tipo)
        elif op == "2":
            listar_metodos_pago(session)
        elif op == "3":
            listar_metodos_pago(session)
            mid = int(input("ID a editar: "))
            tipo = input("Nuevo tipo: ")
            editar_metodo_pago(session, mid, tipo)
        elif op == "4":
            listar_metodos_pago(session)
            mid = int(input("ID a eliminar: "))
            if input("¿Seguro? (s/n): ").lower() == "s":
                eliminar_metodo_pago(session, mid)
        elif op == "0":
            break


def flujo_mantenimiento(session):
    while True:
        op = menu_crud("Mantenimientos")
        if op == "1":
            listar_vehiculos(session)
            vid = int(input("ID del vehículo: "))
            listar_usuarios(session)
            uid = int(input("ID del usuario que registra: "))
            motivo = input("Motivo: ")
            fecha_str = input("Fecha (YYYY-MM-DD): ")
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
            estado = input("Estado [Pendiente]: ") or "Pendiente"
            crear_mantenimiento(session, vid, motivo, fecha, estado, uid)
        elif op == "2":
            listar_mantenimientos(session)
        elif op == "3":
            listar_mantenimientos(session)
            mid = int(input("ID del mantenimiento a editar: "))
            listar_usuarios(session)
            uid = int(input("ID del usuario que edita: "))
            estado = input("Nuevo estado: ").strip()
            motivo = input("Nuevo motivo: ").strip()
            cambios = {}
            if estado:
                cambios["estado"] = estado
            if motivo:
                cambios["motivo"] = motivo
            editar_mantenimiento(session, mid, uid, **cambios)
        elif op == "4":
            listar_mantenimientos(session)
            mid = int(input("ID a eliminar: "))
            if input("¿Seguro? (s/n): ").lower() == "s":
                eliminar_mantenimiento(session, mid)
        elif op == "0":
            break


def flujo_venta(session):
    while True:
        op = menu_crud("Ventas")
        if op == "1":
            listar_empleados(session)
            eid = int(input("ID del empleado (vendedor): "))
            listar_clientes(session)
            cid = int(input("ID del cliente: "))
            listar_vehiculos(session)
            vid = int(input("ID del vehículo: "))
            listar_metodos_pago(session)
            mpid = int(input("ID del método de pago: "))
            listar_usuarios(session)
            uid = int(input("ID del usuario que registra: "))
            fecha_str = input("Fecha (YYYY-MM-DD): ")
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
            precio = float(input("Precio final: "))
            crear_venta(session, eid, cid, vid, mpid, fecha, precio, uid)
        elif op == "2":
            listar_ventas(session)
        elif op == "3":
            listar_ventas(session)
            vid = int(input("ID de la venta a editar: "))
            listar_usuarios(session)
            uid = int(input("ID del usuario que edita: "))
            precio = input("Nuevo precio final: ").strip()
            cambios = {}
            if precio:
                cambios["precio_final"] = float(precio)
            editar_venta(session, vid, uid, **cambios)
        elif op == "4":
            listar_ventas(session)
            vid = int(input("ID de la venta a eliminar: "))
            if input("¿Seguro? (s/n): ").lower() == "s":
                eliminar_venta(session, vid)
        elif op == "0":
            break


if __name__ == "__main__":
    session = get_session()
    try:
        while True:
            opcion = menu_principal()
            if opcion == "1":
                flujo_usuario(session)
            elif opcion == "2":
                flujo_cliente(session)
            elif opcion == "3":
                flujo_empleado(session)
            elif opcion == "4":
                flujo_vehiculo(session)
            elif opcion == "5":
                flujo_metodo_pago(session)
            elif opcion == "6":
                flujo_mantenimiento(session)
            elif opcion == "7":
                flujo_venta(session)
            elif opcion == "0":
                print("\n ¡Hasta luego!")
                break
            else:
                print(" Opción inválida.")
    finally:
        session.close()
