from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session
from src.entities.databases.conexion import SessionLocal
from src.entities.crud.crud_venta import (
    crear_venta,
    listar_ventas,
    editar_venta,
    eliminar_venta,
)

routers = APIRouter(prefix="/ventas", tags=["Ventas"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class VentaCreate(BaseModel):
    empleado_id: int
    cliente_id: int
    vehiculo_id: int
    metodo_pago_id: int
    fecha: datetime
    precio_final: float
    id_usuario_creacion: int


class VentaUpdate(BaseModel):
    precio_final: float | None = None
    id_usuario_edita: int


@routers.get("/")
def listar(db: Session = Depends(get_db)):
    return listar_ventas(db)


@routers.get("/{venta_id}")
def obtener(venta_id: int, db: Session = Depends(get_db)):
    from src.entities.venta import Venta

    venta = db.query(Venta).filter(Venta.id == venta_id).first()
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return venta


@routers.post("/", status_code=201)
def crear(data: VentaCreate, db: Session = Depends(get_db)):
    return crear_venta(
        db,
        data.empleado_id,
        data.cliente_id,
        data.vehiculo_id,
        data.metodo_pago_id,
        data.fecha,
        data.precio_final,
        data.id_usuario_creacion,
    )


@routers.put("/{venta_id}")
def editar(venta_id: int, data: VentaUpdate, db: Session = Depends(get_db)):
    cambios = data.model_dump(exclude={"id_usuario_edita"}, exclude_none=True)
    resultado = editar_venta(db, venta_id, data.id_usuario_edita, **cambios)
    if not resultado:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return resultado


@routers.delete("/{venta_id}")
def eliminar(venta_id: int, db: Session = Depends(get_db)):
    from src.entities.venta import Venta

    venta = db.query(Venta).filter(Venta.id == venta_id).first()
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    eliminar_venta(db, venta_id)
    return {"mensaje": f"Venta {venta_id} eliminada correctamente"}
