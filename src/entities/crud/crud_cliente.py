from sqlalchemy.orm import Session
from src.entities.cliente import Cliente


def crear_cliente(session: Session, nombre: str, telefono: str, correo: str, id_usuario_creacion: int) -> Cliente:
    cliente = Cliente(nombre=nombre, telefono=telefono, correo=correo, id_usuario_creacion=id_usuario_creacion)
    session.add(cliente)
    session.commit()
    session.refresh(cliente)
    print(f" Cliente creado: {cliente.nombre} (ID: {cliente.id})")
    return cliente


def listar_clientes(session: Session):
    clientes = session.query(Cliente).all()
    print(f"\n CLIENTES ({len(clientes)} registros):")
    print("-" * 60)
    for c in clientes:
        print(f"  ID: {c.id} | Nombre: {c.nombre} | Teléfono: {c.telefono} | Correo: {c.correo}")
    return clientes


def editar_cliente(session: Session, cliente_id: int, id_usuario_edita: int, **kwargs) -> Cliente:
    cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        print(f" Cliente con ID {cliente_id} no encontrado.")
        return None
    for key, value in kwargs.items():
        if hasattr(cliente, key):
            setattr(cliente, key, value)
    cliente.id_usuario_edita = id_usuario_edita
    session.commit()
    session.refresh(cliente)
    print(f" Cliente actualizado: {cliente.nombre} (ID: {cliente.id})")
    return cliente


def eliminar_cliente(session: Session, cliente_id: int):
    cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        print(f" Cliente con ID {cliente_id} no encontrado.")
        return
    session.delete(cliente)
    session.commit()
    print(f"  Cliente eliminado (ID: {cliente_id})")