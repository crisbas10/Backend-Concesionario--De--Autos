from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.entities.databases.conexion import SessionLocal
from src.entities.crud.crud_empleado import (
    crear_empleado,
    listar_empleados,
    editar_empleado,
    eliminar_empleado,
)
 
router = APIRouter(prefix="/empleados", tags=["Empleados"])
 
 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
 
class EmpleadoCreate(BaseModel):
    nombre: str
    telefono: str
    correo: str
    salario: float
    cargo: str
 
 
class EmpleadoUpdate(BaseModel):
    nombre: str | None = None
    telefono: str | None = None
    correo: str | None = None
    salario: float | None = None
    cargo: str | None = None
 
 
@router.get("/")
def listar(db: Session = Depends(get_db)):
    return listar_empleados(db)
 
 
@router.get("/{empleado_id}")
def obtener(empleado_id: int, db: Session = Depends(get_db)):
    from src.entities.empleado import Empleado
    empleado = db.query(Empleado).filter(Empleado.id == empleado_id).first()
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado
 
 
@router.post("/", status_code=201)
def crear(data: EmpleadoCreate, db: Session = Depends(get_db)):
    return crear_empleado(db, data.nombre, data.telefono, data.correo, data.salario, data.cargo)
 
 
@router.put("/{empleado_id}")
def editar(empleado_id: int, data: EmpleadoUpdate, db: Session = Depends(get_db)):
    cambios = data.model_dump(exclude_none=True)
    resultado = editar_empleado(db, empleado_id, **cambios)
    if not resultado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return resultado
 
 
@router.delete("/{empleado_id}")
def eliminar(empleado_id: int, db: Session = Depends(get_db)):
    from src.entities.empleado import Empleado
    empleado = db.query(Empleado).filter(Empleado.id == empleado_id).first()
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    eliminar_empleado(db, empleado_id)
    return {"mensaje": f"Empleado {empleado_id} eliminado correctamente"}