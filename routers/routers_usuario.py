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
 
router = APIRouter(prefix="/usuarios", tags=["Usuarios"])
 
 
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
 
 
@router.get("/")

def listar(db: Session = Depends(get_db)):

    return listar_usuarios(db)
 
 
@router.get("/{usuario_id}")

def obtener(usuario_id: int, db: Session = Depends(get_db)):

    from src.entities.usuario import Usuario

    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    if not usuario:

        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return usuario
 
 
@router.post("/", status_code=201)

def crear(data: UsuarioCreate, db: Session = Depends(get_db)):

    return crear_usuario(db, data.nombre_usuario, data.correo, data.password, data.rol)
 
 
@router.put("/{usuario_id}")

def editar(usuario_id: int, data: UsuarioUpdate, db: Session = Depends(get_db)):

    cambios = data.model_dump(exclude_none=True)

    resultado = editar_usuario(db, usuario_id, **cambios)

    if not resultado:

        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return resultado
 
 
@router.delete("/{usuario_id}")

def eliminar(usuario_id: int, db: Session = Depends(get_db)):

    from src.entities.usuario import Usuario

    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    if not usuario:

        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    eliminar_usuario(db, usuario_id)

    return {"mensaje": f"Usuario {usuario_id} eliminado correctamente"}
 
cliente
 
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
 
empleado
 
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
 