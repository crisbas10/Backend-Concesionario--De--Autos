from datetime import datetime
from sqlalchemy.orm import Session
from src.entities.Mantenimiento import Mantenimiento


def crear_mantenimiento(
    session: Session,
    vehiculo_id: int,
    motivo: str,
    fecha: datetime,
    estado: str,
    id_usuario_creacion: int,
) -> Mantenimiento:
    mantenimiento = Mantenimiento(
        vehiculo_id=vehiculo_id,
        motivo=motivo,
        fecha=fecha,
        estado=estado,
        id_usuario_creacion=id_usuario_creacion,
    )
    session.add(mantenimiento)
    session.commit()
    session.refresh(mantenimiento)
    print(f" Mantenimiento creado: {mantenimiento.motivo} (ID: {mantenimiento.id})")
    return mantenimiento


def listar_mantenimientos(session: Session):
    mantenimientos = session.query(Mantenimiento).all()
    print(f"\n MANTENIMIENTOS ({len(mantenimientos)} registros):")
    print("-" * 60)
    for m in mantenimientos:
        print(
            f"  ID: {m.id} | Vehículo ID: {m.vehiculo_id} | Motivo: {m.motivo} | Estado: {m.estado} | Fecha: {m.fecha}"
        )
    return mantenimientos


def editar_mantenimiento(
    session: Session, mantenimiento_id: int, id_usuario_edita: int, **kwargs
) -> Mantenimiento:
    mantenimiento = (
        session.query(Mantenimiento)
        .filter(Mantenimiento.id == mantenimiento_id)
        .first()
    )
    if not mantenimiento:
        print(f" Mantenimiento con ID {mantenimiento_id} no encontrado.")
        return None
    for key, value in kwargs.items():
        if hasattr(mantenimiento, key):
            setattr(mantenimiento, key, value)
    mantenimiento.id_usuario_edita = id_usuario_edita
    session.commit()
    session.refresh(mantenimiento)
    print(f" Mantenimiento actualizado (ID: {mantenimiento.id})")
    return mantenimiento


def eliminar_mantenimiento(session: Session, mantenimiento_id: int):
    mantenimiento = (
        session.query(Mantenimiento)
        .filter(Mantenimiento.id == mantenimiento_id)
        .first()
    )
    if not mantenimiento:
        print(f" Mantenimiento con ID {mantenimiento_id} no encontrado.")
        return
    session.delete(mantenimiento)
    session.commit()
    print(f"  Mantenimiento eliminado (ID: {mantenimiento_id})")
