from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.entities.databases.conexion import SessionLocal
from src.entities.crud.crud_metodo_pago import (
    crear_metodo_pago,
    listar_metodos_pago,
    editar_metodo_pago,
    eliminar_metodo_pago,
)

routers = APIRouter(prefix="/metodos-pago", tags=["Métodos de Pago"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class MetodoPagoCreate(BaseModel):
    tipo: str


class MetodoPagoUpdate(BaseModel):
    tipo: str


@routers.get("/")
def listar(db: Session = Depends(get_db)):
    return listar_metodos_pago(db)


@routers.get("/{metodo_id}")
def obtener(metodo_id: int, db: Session = Depends(get_db)):
    from src.entities.metodo_pago import MetodoPago

    metodo = db.query(MetodoPago).filter(MetodoPago.id == metodo_id).first()
    if not metodo:
        raise HTTPException(status_code=404, detail="Método de pago no encontrado")
    return metodo


@routers.post("/", status_code=201)
def crear(data: MetodoPagoCreate, db: Session = Depends(get_db)):
    return crear_metodo_pago(db, data.tipo)


@routers.put("/{metodo_id}")
def editar(metodo_id: int, data: MetodoPagoUpdate, db: Session = Depends(get_db)):
    resultado = editar_metodo_pago(db, metodo_id, data.tipo)
    if not resultado:
        raise HTTPException(status_code=404, detail="Método de pago no encontrado")
    return resultado


@routers.delete("/{metodo_id}")
def eliminar(metodo_id: int, db: Session = Depends(get_db)):
    from src.entities.metodo_pago import MetodoPago

    metodo = db.query(MetodoPago).filter(MetodoPago.id == metodo_id).first()
    if not metodo:
        raise HTTPException(status_code=404, detail="Método de pago no encontrado")
    eliminar_metodo_pago(db, metodo_id)
    return {"mensaje": f"Método de pago {metodo_id} eliminado correctamente"}
