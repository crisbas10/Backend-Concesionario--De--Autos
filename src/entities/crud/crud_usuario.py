from sqlalchemy.orm import Session
from src.entities.usuario import Usuario


def crear_usuario(session: Session, nombre_usuario: str, correo: str, password: str, rol: str = "vendedor") -> Usuario:
    usuario = Usuario(nombre_usuario=nombre_usuario, correo=correo, password=password, rol=rol)
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    print(f" Usuario creado: {usuario.nombre_usuario} (ID: {usuario.id})")
    return usuario


def listar_usuarios(session: Session):
    usuarios = session.query(Usuario).all()
    print(f"\n USUARIOS ({len(usuarios)} registros):")
    print("-" * 60)
    for u in usuarios:
        print(f"  ID: {u.id} | Usuario: {u.nombre_usuario} | Correo: {u.correo} | Rol: {u.rol}")
    return usuarios


def editar_usuario(session: Session, usuario_id: int, **kwargs) -> Usuario:
    usuario = session.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        print(f" Usuario con ID {usuario_id} no encontrado.")
        return None
    for key, value in kwargs.items():
        if hasattr(usuario, key):
            setattr(usuario, key, value)
    session.commit()
    session.refresh(usuario)
    print(f" Usuario actualizado: {usuario.nombre_usuario} (ID: {usuario.id})")
    return usuario


def eliminar_usuario(session: Session, usuario_id: int):
    usuario = session.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        print(f" Usuario con ID {usuario_id} no encontrado.")
        return
    session.delete(usuario)
    session.commit()
    print(f"  Usuario eliminado (ID: {usuario_id})")