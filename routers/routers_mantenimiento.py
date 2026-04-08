from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session
from src.entities.databases.conexion import SessionLocal
from src.entities.crud.crud_Mantenimiento import (
    crear_mantenimiento,
    listar_mantenimientos,
    editar_mantenimiento,
    eliminar_mantenimiento,
)

router = APIRouter(prefix="/mantenimientos", tags=["Mantenimientos"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class MantenimientoCreate(BaseModel):
    vehiculo_id: int
    motivo: str
    fecha: datetime
    estado: str
    id_usuario_creacion: int


class MantenimientoUpdate(BaseModel):
    motivo: str | None = None
    estado: str | None = None
    id_usuario_edita: int


@router.get("/")
def listar(db: Session = Depends(get_db)):
    return listar_mantenimientos(db)


@router.get("/{mantenimiento_id}")
def obtener(mantenimiento_id: int, db: Session = Depends(get_db)):
    from src.entities.Mantenimiento import Mantenimiento

    m = db.query(Mantenimiento).filter(Mantenimiento.id == mantenimiento_id).first()
    if not m:
        raise HTTPException(status_code=404, detail="Mantenimiento no encontrado")
    return m


@router.post("/", status_code=201)
def crear(data: MantenimientoCreate, db: Session = Depends(get_db)):
    return crear_mantenimiento(
        db,
        data.vehiculo_id,
        data.motivo,
        data.fecha,
        data.estado,
        data.id_usuario_creacion,
    )


@router.put("/{mantenimiento_id}")
def editar(
    mantenimiento_id: int, data: MantenimientoUpdate, db: Session = Depends(get_db)
):
    cambios = data.model_dump(exclude={"id_usuario_edita"}, exclude_none=True)
    resultado = editar_mantenimiento(
        db, mantenimiento_id, data.id_usuario_edita, **cambios
    )
    if not resultado:
        raise HTTPException(status_code=404, detail="Mantenimiento no encontrado")
    return resultado


@router.delete("/{mantenimiento_id}")
def eliminar(mantenimiento_id: int, db: Session = Depends(get_db)):
    from src.entities.Mantenimiento import Mantenimiento

    m = db.query(Mantenimiento).filter(Mantenimiento.id == mantenimiento_id).first()
    if not m:
        raise HTTPException(status_code=404, detail="Mantenimiento no encontrado")
    eliminar_mantenimiento(db, mantenimiento_id)
    return {"mensaje": f"Mantenimiento {mantenimiento_id} eliminado correctamente"}
