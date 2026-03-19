from sqlalchemy.orm import Session
from src.entities.empleado import Empleado


def crear_empleado(session: Session, nombre: str, telefono: str, correo: str, salario: float, cargo: str) -> Empleado:
    empleado = Empleado(nombre=nombre, telefono=telefono, correo=correo, salario=salario, cargo=cargo)
    session.add(empleado)
    session.commit()
    session.refresh(empleado)
    print(f" Empleado creado: {empleado.nombre} - {empleado.cargo} (ID: {empleado.id})")
    return empleado


def listar_empleados(session: Session):
    empleados = session.query(Empleado).all()
    print(f"\n EMPLEADOS ({len(empleados)} registros):")
    print("-" * 60)
    for e in empleados:
        print(f"  ID: {e.id} | Nombre: {e.nombre} | Cargo: {e.cargo} | Salario: ${e.salario:,.2f}")
    return empleados


def editar_empleado(session: Session, empleado_id: int, **kwargs) -> Empleado:
    empleado = session.query(Empleado).filter(Empleado.id == empleado_id).first()
    if not empleado:
        print(f" Empleado con ID {empleado_id} no encontrado.")
        return None
    for key, value in kwargs.items():
        if hasattr(empleado, key):
            setattr(empleado, key, value)
    session.commit()
    session.refresh(empleado)
    print(f" Empleado actualizado: {empleado.nombre} (ID: {empleado.id})")
    return empleado


def eliminar_empleado(session: Session, empleado_id: int):
    empleado = session.query(Empleado).filter(Empleado.id == empleado_id).first()
    if not empleado:
        print(f" Empleado con ID {empleado_id} no encontrado.")
        return
    session.delete(empleado)
    session.commit()
    print(f"  Empleado eliminado (ID: {empleado_id})")