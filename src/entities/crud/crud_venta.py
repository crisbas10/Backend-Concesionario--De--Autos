from datetime import datetime
from sqlalchemy.orm import Session
from src.entities.venta import Venta


def crear_venta(
    session: Session,
    empleado_id: int,
    cliente_id: int,
    vehiculo_id: int,
    metodo_pago_id: int,
    fecha: datetime,
    precio_final: float,
    id_usuario_creacion: int,
) -> Venta:
    venta = Venta(
        empleado_id=empleado_id,
        cliente_id=cliente_id,
        vehiculo_id=vehiculo_id,
        metodo_pago_id=metodo_pago_id,
        fecha=fecha,
        precio_final=precio_final,
        id_usuario_creacion=id_usuario_creacion,
    )
    session.add(venta)
    session.commit()
    session.refresh(venta)
    print(f"Venta creada: ID {venta.id} | Precio: ${venta.precio_final:,.2f}")
    return venta


def listar_ventas(session: Session):
    ventas = session.query(Venta).all()
    print(f"\n VENTAS ({len(ventas)} registros):")
    print("-" * 60)
    for v in ventas:
        print(
            f"  ID: {v.id} | Empleado: {v.empleado_id} | Cliente: {v.cliente_id} | Vehículo: {v.vehiculo_id} | Precio: ${v.precio_final:,.2f} | Fecha: {v.fecha}"
        )
    return ventas


def editar_venta(
    session: Session, venta_id: int, id_usuario_edita: int, **kwargs
) -> Venta:
    venta = session.query(Venta).filter(Venta.id == venta_id).first()
    if not venta:
        print(f" Venta con ID {venta_id} no encontrada.")
        return None
    for key, value in kwargs.items():
        if hasattr(venta, key):
            setattr(venta, key, value)
    venta.id_usuario_edita = id_usuario_edita
    session.commit()
    session.refresh(venta)
    print(f" Venta actualizada (ID: {venta.id})")
    return venta


def eliminar_venta(session: Session, venta_id: int):
    venta = session.query(Venta).filter(Venta.id == venta_id).first()
    if not venta:
        print(f" Venta con ID {venta_id} no encontrada.")
        return
    session.delete(venta)
    session.commit()
    print(f"  Venta eliminada (ID: {venta_id})")
