from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.entities.databases.conexion import SessionLocal
from src.entities.crud.crud_cliente import (
    crear_cliente,
    listar_clientes,
    editar_cliente,
    eliminar_cliente,
)
from src.entities.crud.crud_cliente import (
    crear_cliente,
    listar_clientes,
    editar_cliente,
    eliminar_cliente,
)
 
router = APIRouter(prefix="/clientes", tags=["Clientes"])
 
 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
 
class ClienteCreate(BaseModel):
    nombre: str
    telefono: str
    correo: str
    id_usuario_creacion: int
 
 
class ClienteUpdate(BaseModel):
    nombre: str | None = None
    telefono: str | None = None
    correo: str | None = None
    id_usuario_edita: int
 
 
@router.get("/")
def listar(db: Session = Depends(get_db)):
    return listar_clientes(db)
 
 
@router.get("/{cliente_id}")
def obtener(cliente_id: int, db: Session = Depends(get_db)):
    from src.entities.cliente import Cliente
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente
 
 
@router.post("/", status_code=201)
def crear(data: ClienteCreate, db: Session = Depends(get_db)):
    return crear_cliente(db, data.nombre, data.telefono, data.correo, data.id_usuario_creacion)
 
 
@router.put("/{cliente_id}")
def editar(cliente_id: int, data: ClienteUpdate, db: Session = Depends(get_db)):
    cambios = data.model_dump(exclude={"id_usuario_edita"}, exclude_none=True)
    resultado = editar_cliente(db, cliente_id, data.id_usuario_edita, **cambios)
    if not resultado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return resultado
 
 
@router.delete("/{cliente_id}")
def eliminar(cliente_id: int, db: Session = Depends(get_db)):
    from src.entities.cliente import Cliente
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    eliminar_cliente(db, cliente_id)
    return {"mensaje": f"Cliente {cliente_id} eliminado correctamente"}