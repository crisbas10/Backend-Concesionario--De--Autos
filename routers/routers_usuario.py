from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.entities.databases.conexion import SessionLocal
from src.entities.crud.crud_usuario import (
    crear_usuario,
    listar_usuarios,
    editar_usuario,
    eliminar_usuario,
)

routers = APIRouter(prefix="/usuarios", tags=["Usuarios"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class UsuarioCreate(BaseModel):
    nombre_usuario: str
    correo: str
    password: str
    rol: str = "vendedor"


class UsuarioUpdate(BaseModel):
    nombre_usuario: str | None = None
    correo: str | None = None
    password: str | None = None
    rol: str | None = None


@routers.get("/")
def listar(db: Session = Depends(get_db)):
    return listar_usuarios(db)


@routers.get("/{usuario_id}")
def obtener(usuario_id: int, db: Session = Depends(get_db)):
    from src.entities.usuario import Usuario

    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@routers.post("/", status_code=201)
def crear(data: UsuarioCreate, db: Session = Depends(get_db)):
    return crear_usuario(db, data.nombre_usuario, data.correo, data.password, data.rol)


@routers.put("/{usuario_id}")
def editar(usuario_id: int, data: UsuarioUpdate, db: Session = Depends(get_db)):
    cambios = data.model_dump(exclude_none=True)
    resultado = editar_usuario(db, usuario_id, **cambios)
    if not resultado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return resultado


@routers.delete("/{usuario_id}")
def eliminar(usuario_id: int, db: Session = Depends(get_db)):
    from src.entities.usuario import Usuario

    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    eliminar_usuario(db, usuario_id)
    return {"mensaje": f"Usuario {usuario_id} eliminado correctamente"}
