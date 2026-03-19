from datetime import datetime
from sqlalchemy.orm import Session
from src.entities.usuario import Usuario
from src.entities.cliente import Cliente
from src.entities.empleado import Empleado
from src.entities.vehiculo import Vehiculo
from src.entities.metodo_pago import MetodoPago
from src.entities.Mantenimiento import Mantenimiento
from src.entities.venta import Venta


# =============================================================================
# USUARIO
# =============================================================================

def crear_usuario(session: Session, nombre_usuario: str, correo: str, password: str, rol: str = "vendedor") -> Usuario:
    usuario = Usuario(nombre_usuario=nombre_usuario, correo=correo, password=password, rol=rol)
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    print(f"✅ Usuario creado: {usuario.nombre_usuario} (ID: {usuario.id})")
    return usuario

def listar_usuarios(session: Session):
    usuarios = session.query(Usuario).all()
    print(f"\n📋 USUARIOS ({len(usuarios)} registros):")
    print("-" * 60)
    for u in usuarios:
        print(f"  ID: {u.id} | Usuario: {u.nombre_usuario} | Correo: {u.correo} | Rol: {u.rol}")
    return usuarios

def editar_usuario(session: Session, usuario_id: int, **kwargs) -> Usuario:
    usuario = session.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        print(f"❌ Usuario con ID {usuario_id} no encontrado.")
        return None
    for key, value in kwargs.items():
        if hasattr(usuario, key):
            setattr(usuario, key, value)
    session.commit()
    session.refresh(usuario)
    print(f"✅ Usuario actualizado: {usuario.nombre_usuario} (ID: {usuario.id})")
    return usuario

def eliminar_usuario(session: Session, usuario_id: int):
    usuario = session.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        print(f"❌ Usuario con ID {usuario_id} no encontrado.")
        return
    session.delete(usuario)
    session.commit()
    print(f"🗑️  Usuario eliminado (ID: {usuario_id})")


# =============================================================================
# CLIENTE
# =============================================================================

def crear_cliente(session: Session, nombre: str, telefono: str, correo: str, id_usuario_creacion: int) -> Cliente:
    cliente = Cliente(nombre=nombre, telefono=telefono, correo=correo, id_usuario_creacion=id_usuario_creacion)
    session.add(cliente)
    session.commit()
    session.refresh(cliente)
    print(f"✅ Cliente creado: {cliente.nombre} (ID: {cliente.id})")
    return cliente

def listar_clientes(session: Session):
    clientes = session.query(Cliente).all()
    print(f"\n📋 CLIENTES ({len(clientes)} registros):")
    print("-" * 60)
    for c in clientes:
        print(f"  ID: {c.id} | Nombre: {c.nombre} | Teléfono: {c.telefono} | Correo: {c.correo}")
    return clientes

def editar_cliente(session: Session, cliente_id: int, id_usuario_edita: int, **kwargs) -> Cliente:
    cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        print(f"❌ Cliente con ID {cliente_id} no encontrado.")
        return None
    for key, value in kwargs.items():
        if hasattr(cliente, key):
            setattr(cliente, key, value)
    cliente.id_usuario_edita = id_usuario_edita
    session.commit()
    session.refresh(cliente)
    print(f"✅ Cliente actualizado: {cliente.nombre} (ID: {cliente.id})")
    return cliente

def eliminar_cliente(session: Session, cliente_id: int):
    cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        print(f"❌ Cliente con ID {cliente_id} no encontrado.")
        return
    session.delete(cliente)
    session.commit()
    print(f"🗑️  Cliente eliminado (ID: {cliente_id})")


# =============================================================================
# EMPLEADO
# =============================================================================

def crear_empleado(session: Session, nombre: str, telefono: str, correo: str, salario: float, cargo: str) -> Empleado:
    empleado = Empleado(nombre=nombre, telefono=telefono, correo=correo, salario=salario, cargo=cargo)
    session.add(empleado)
    session.commit()
    session.refresh(empleado)
    print(f"✅ Empleado creado: {empleado.nombre} - {empleado.cargo} (ID: {empleado.id})")
    return empleado

def listar_empleados(session: Session):
    empleados = session.query(Empleado).all()
    print(f"\n📋 EMPLEADOS ({len(empleados)} registros):")
    print("-" * 60)
    for e in empleados:
        print(f"  ID: {e.id} | Nombre: {e.nombre} | Cargo: {e.cargo} | Salario: ${e.salario:,.2f}")
    return empleados

def editar_empleado(session: Session, empleado_id: int, **kwargs) -> Empleado:
    empleado = session.query(Empleado).filter(Empleado.id == empleado_id).first()
    if not empleado:
        print(f"❌ Empleado con ID {empleado_id} no encontrado.")
        return None
    for key, value in kwargs.items():
        if hasattr(empleado, key):
            setattr(empleado, key, value)
    session.commit()
    session.refresh(empleado)
    print(f"✅ Empleado actualizado: {empleado.nombre} (ID: {empleado.id})")
    return empleado

def eliminar_empleado(session: Session, empleado_id: int):
    empleado = session.query(Empleado).filter(Empleado.id == empleado_id).first()
    if not empleado:
        print(f"❌ Empleado con ID {empleado_id} no encontrado.")
        return
    session.delete(empleado)
    session.commit()
    print(f"🗑️  Empleado eliminado (ID: {empleado_id})")


# =============================================================================
# VEHICULO
# =============================================================================

def crear_vehiculo(session: Session, marca: str, modelo: str, anio: int, precio: float,
                   kilometraje: int, estado: str, disponibilidad: bool, id_usuario_creacion: int) -> Vehiculo:
    vehiculo = Vehiculo(marca=marca, modelo=modelo, anio=anio, precio=precio,
                        kilometraje=kilometraje, estado=estado, disponibilidad=disponibilidad,
                        id_usuario_creacion=id_usuario_creacion)
    session.add(vehiculo)
    session.commit()
    session.refresh(vehiculo)
    print(f"✅ Vehículo creado: {vehiculo.marca} {vehiculo.modelo} {vehiculo.anio} (ID: {vehiculo.id})")
    return vehiculo

def listar_vehiculos(session: Session):
    vehiculos = session.query(Vehiculo).all()
    print(f"\n📋 VEHÍCULOS ({len(vehiculos)} registros):")
    print("-" * 60)
    for v in vehiculos:
        disp = "Disponible" if v.disponibilidad else "No disponible"
        print(f"  ID: {v.id} | {v.marca} {v.modelo} {v.anio} | ${v.precio:,.2f} | {v.estado} | {disp}")
    return vehiculos

def editar_vehiculo(session: Session, vehiculo_id: int, id_usuario_edita: int, **kwargs) -> Vehiculo:
    vehiculo = session.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).first()
    if not vehiculo:
        print(f"❌ Vehículo con ID {vehiculo_id} no encontrado.")
        return None
    for key, value in kwargs.items():
        if hasattr(vehiculo, key):
            setattr(vehiculo, key, value)
    vehiculo.id_usuario_edita = id_usuario_edita
    session.commit()
    session.refresh(vehiculo)
    print(f"✅ Vehículo actualizado: {vehiculo.marca} {vehiculo.modelo} (ID: {vehiculo.id})")
    return vehiculo

def eliminar_vehiculo(session: Session, vehiculo_id: int):
    vehiculo = session.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).first()
    if not vehiculo:
        print(f"❌ Vehículo con ID {vehiculo_id} no encontrado.")
        return
    session.delete(vehiculo)
    session.commit()
    print(f"🗑️  Vehículo eliminado (ID: {vehiculo_id})")


# =============================================================================
# METODO DE PAGO
# =============================================================================

def crear_metodo_pago(session: Session, tipo: str) -> MetodoPago:
    metodo = MetodoPago(tipo=tipo)
    session.add(metodo)
    session.commit()
    session.refresh(metodo)
    print(f"✅ Método de pago creado: {metodo.tipo} (ID: {metodo.id})")
    return metodo

def listar_metodos_pago(session: Session):
    metodos = session.query(MetodoPago).all()
    print(f"\n📋 MÉTODOS DE PAGO ({len(metodos)} registros):")
    print("-" * 60)
    for m in metodos:
        print(f"  ID: {m.id} | Tipo: {m.tipo}")
    return metodos

def editar_metodo_pago(session: Session, metodo_id: int, tipo: str) -> MetodoPago:
    metodo = session.query(MetodoPago).filter(MetodoPago.id == metodo_id).first()
    if not metodo:
        print(f"❌ Método de pago con ID {metodo_id} no encontrado.")
        return None
    metodo.tipo = tipo
    session.commit()
    session.refresh(metodo)
    print(f"✅ Método de pago actualizado: {metodo.tipo} (ID: {metodo.id})")
    return metodo

def eliminar_metodo_pago(session: Session, metodo_id: int):
    metodo = session.query(MetodoPago).filter(MetodoPago.id == metodo_id).first()
    if not metodo:
        print(f"❌ Método de pago con ID {metodo_id} no encontrado.")
        return
    session.delete(metodo)
    session.commit()
    print(f"🗑️  Método de pago eliminado (ID: {metodo_id})")


# =============================================================================
# MANTENIMIENTO
# =============================================================================

def crear_mantenimiento(session: Session, vehiculo_id: int, motivo: str,
                        fecha: datetime, estado: str, id_usuario_creacion: int) -> Mantenimiento:
    mantenimiento = Mantenimiento(vehiculo_id=vehiculo_id, motivo=motivo, fecha=fecha,
                                  estado=estado, id_usuario_creacion=id_usuario_creacion)
    session.add(mantenimiento)
    session.commit()
    session.refresh(mantenimiento)
    print(f"✅ Mantenimiento creado: {mantenimiento.motivo} (ID: {mantenimiento.id})")
    return mantenimiento

def listar_mantenimientos(session: Session):
    mantenimientos = session.query(Mantenimiento).all()
    print(f"\n📋 MANTENIMIENTOS ({len(mantenimientos)} registros):")
    print("-" * 60)
    for m in mantenimientos:
        print(f"  ID: {m.id} | Vehículo ID: {m.vehiculo_id} | Motivo: {m.motivo} | Estado: {m.estado} | Fecha: {m.fecha}")
    return mantenimientos

def editar_mantenimiento(session: Session, mantenimiento_id: int, id_usuario_edita: int, **kwargs) -> Mantenimiento:
    mantenimiento = session.query(Mantenimiento).filter(Mantenimiento.id == mantenimiento_id).first()
    if not mantenimiento:
        print(f"❌ Mantenimiento con ID {mantenimiento_id} no encontrado.")
        return None
    for key, value in kwargs.items():
        if hasattr(mantenimiento, key):
            setattr(mantenimiento, key, value)
    mantenimiento.id_usuario_edita = id_usuario_edita
    session.commit()
    session.refresh(mantenimiento)
    print(f"✅ Mantenimiento actualizado (ID: {mantenimiento.id})")
    return mantenimiento

def eliminar_mantenimiento(session: Session, mantenimiento_id: int):
    mantenimiento = session.query(Mantenimiento).filter(Mantenimiento.id == mantenimiento_id).first()
    if not mantenimiento:
        print(f"❌ Mantenimiento con ID {mantenimiento_id} no encontrado.")
        return
    session.delete(mantenimiento)
    session.commit()
    print(f"🗑️  Mantenimiento eliminado (ID: {mantenimiento_id})")


# =============================================================================
# VENTA
# =============================================================================

def crear_venta(session: Session, empleado_id: int, cliente_id: int, vehiculo_id: int,
                metodo_pago_id: int, fecha: datetime, precio_final: float, id_usuario_creacion: int) -> Venta:
    venta = Venta(empleado_id=empleado_id, cliente_id=cliente_id, vehiculo_id=vehiculo_id,
                  metodo_pago_id=metodo_pago_id, fecha=fecha, precio_final=precio_final,
                  id_usuario_creacion=id_usuario_creacion)
    session.add(venta)
    session.commit()
    session.refresh(venta)
    print(f"✅ Venta creada: ID {venta.id} | Precio: ${venta.precio_final:,.2f}")
    return venta

def listar_ventas(session: Session):
    ventas = session.query(Venta).all()
    print(f"\n📋 VENTAS ({len(ventas)} registros):")
    print("-" * 60)
    for v in ventas:
        print(f"  ID: {v.id} | Empleado: {v.empleado_id} | Cliente: {v.cliente_id} | Vehículo: {v.vehiculo_id} | Precio: ${v.precio_final:,.2f} | Fecha: {v.fecha}")
    return ventas

def editar_venta(session: Session, venta_id: int, id_usuario_edita: int, **kwargs) -> Venta:
    venta = session.query(Venta).filter(Venta.id == venta_id).first()
    if not venta:
        print(f"❌ Venta con ID {venta_id} no encontrada.")
        return None
    for key, value in kwargs.items():
        if hasattr(venta, key):
            setattr(venta, key, value)
    venta.id_usuario_edita = id_usuario_edita
    session.commit()
    session.refresh(venta)
    print(f"✅ Venta actualizada (ID: {venta.id})")
    return venta

def eliminar_venta(session: Session, venta_id: int):
    venta = session.query(Venta).filter(Venta.id == venta_id).first()
    if not venta:
        print(f"❌ Venta con ID {venta_id} no encontrada.")
        return
    session.delete(venta)
    session.commit()
    print(f"🗑️  Venta eliminada (ID: {venta_id})")
