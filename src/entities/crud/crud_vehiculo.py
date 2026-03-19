from sqlalchemy.orm import Session
from src.entities.vehiculo import Vehiculo


def crear_vehiculo(
    session: Session,
    marca: str,
    modelo: str,
    anio: int,
    precio: float,
    kilometraje: int,
    estado: str,
    disponibilidad: bool,
    id_usuario_creacion: int,
) -> Vehiculo:
    vehiculo = Vehiculo(
        marca=marca,
        modelo=modelo,
        anio=anio,
        precio=precio,
        kilometraje=kilometraje,
        estado=estado,
        disponibilidad=disponibilidad,
        id_usuario_creacion=id_usuario_creacion,
    )
    session.add(vehiculo)
    session.commit()
    session.refresh(vehiculo)
    print(
        f" Vehículo creado: {vehiculo.marca} {vehiculo.modelo} {vehiculo.anio} (ID: {vehiculo.id})"
    )
    return vehiculo


def listar_vehiculos(session: Session):
    vehiculos = session.query(Vehiculo).all()
    print(f"\n VEHÍCULOS ({len(vehiculos)} registros):")
    print("-" * 60)
    for v in vehiculos:
        disp = "Disponible" if v.disponibilidad else "No disponible"
        print(
            f"  ID: {v.id} | {v.marca} {v.modelo} {v.anio} | ${v.precio:,.2f} | {v.estado} | {disp}"
        )
    return vehiculos


def editar_vehiculo(
    session: Session, vehiculo_id: int, id_usuario_edita: int, **kwargs
) -> Vehiculo:
    vehiculo = session.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).first()
    if not vehiculo:
        print(f" Vehículo con ID {vehiculo_id} no encontrado.")
        return None
    for key, value in kwargs.items():
        if hasattr(vehiculo, key):
            setattr(vehiculo, key, value)
    vehiculo.id_usuario_edita = id_usuario_edita
    session.commit()
    session.refresh(vehiculo)
    print(
        f" Vehículo actualizado: {vehiculo.marca} {vehiculo.modelo} (ID: {vehiculo.id})"
    )
    return vehiculo


def eliminar_vehiculo(session: Session, vehiculo_id: int):
    vehiculo = session.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).first()
    if not vehiculo:
        print(f" Vehículo con ID {vehiculo_id} no encontrado.")
        return
    session.delete(vehiculo)
    session.commit()
    print(f"  Vehículo eliminado (ID: {vehiculo_id})")
