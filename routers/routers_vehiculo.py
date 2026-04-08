from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.entities.databases.conexion import SessionLocal
from src.entities.crud.crud_vehiculo import (
    crear_vehiculo,
    listar_vehiculos,
    editar_vehiculo,
    eliminar_vehiculo,
)

router = APIRouter(prefix="/vehiculos", tags=["Vehículos"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class VehiculoCreate(BaseModel):
    marca: str
    modelo: str
    anio: int
    precio: float
    kilometraje: int
    estado: str
    disponibilidad: bool
    id_usuario_creacion: int


class VehiculoUpdate(BaseModel):
    marca: str | None = None
    modelo: str | None = None
    anio: int | None = None
    precio: float | None = None
    kilometraje: int | None = None
    estado: str | None = None
    disponibilidad: bool | None = None
    id_usuario_edita: int


@router.get("/")
def listar(db: Session = Depends(get_db)):
    return listar_vehiculos(db)


@router.get("/{vehiculo_id}")
def obtener(vehiculo_id: int, db: Session = Depends(get_db)):
    from src.entities.vehiculo import Vehiculo

    vehiculo = db.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).first()
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return vehiculo


@router.post("/", status_code=201)
def crear(data: VehiculoCreate, db: Session = Depends(get_db)):
    return crear_vehiculo(
        db,
        data.marca,
        data.modelo,
        data.anio,
        data.precio,
        data.kilometraje,
        data.estado,
        data.disponibilidad,
        data.id_usuario_creacion,
    )


@router.put("/{vehiculo_id}")
def editar(vehiculo_id: int, data: VehiculoUpdate, db: Session = Depends(get_db)):
    cambios = data.model_dump(exclude={"id_usuario_edita"}, exclude_none=True)
    resultado = editar_vehiculo(db, vehiculo_id, data.id_usuario_edita, **cambios)
    if not resultado:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return resultado


@router.delete("/{vehiculo_id}")
def eliminar(vehiculo_id: int, db: Session = Depends(get_db)):
    from src.entities.vehiculo import Vehiculo

    vehiculo = db.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).first()
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    eliminar_vehiculo(db, vehiculo_id)
    return {"mensaje": f"Vehículo {vehiculo_id} eliminado correctamente"}
