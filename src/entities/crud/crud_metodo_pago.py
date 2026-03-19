from sqlalchemy.orm import Session
from src.entities.metodo_pago import MetodoPago


def crear_metodo_pago(session: Session, tipo: str) -> MetodoPago:
    metodo = MetodoPago(tipo=tipo)
    session.add(metodo)
    session.commit()
    session.refresh(metodo)
    print(f" Método de pago creado: {metodo.tipo} (ID: {metodo.id})")
    return metodo


def listar_metodos_pago(session: Session):
    metodos = session.query(MetodoPago).all()
    print(f"\n MÉTODOS DE PAGO ({len(metodos)} registros):")
    print("-" * 60)
    for m in metodos:
        print(f"  ID: {m.id} | Tipo: {m.tipo}")
    return metodos


def editar_metodo_pago(session: Session, metodo_id: int, tipo: str) -> MetodoPago:
    metodo = session.query(MetodoPago).filter(MetodoPago.id == metodo_id).first()
    if not metodo:
        print(f" Método de pago con ID {metodo_id} no encontrado.")
        return None
    metodo.tipo = tipo
    session.commit()
    session.refresh(metodo)
    print(f" Método de pago actualizado: {metodo.tipo} (ID: {metodo.id})")
    return metodo


def eliminar_metodo_pago(session: Session, metodo_id: int):
    metodo = session.query(MetodoPago).filter(MetodoPago.id == metodo_id).first()
    if not metodo:
        print(f" Método de pago con ID {metodo_id} no encontrado.")
        return
    session.delete(metodo)
    session.commit()
    print(f"  Método de pago eliminado (ID: {metodo_id})")
