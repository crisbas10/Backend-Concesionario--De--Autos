from fastapi import FastAPI

from src.entities import Base

from src.entities.databases.conexion import engine
 
from routers.router_usuario import router as router_usuario

from routers.router_cliente import router as router_cliente

from routers.router_empleado import router as router_empleado

from routers.router_vehiculo import router as router_vehiculo

from routers.router_metodo_pago import router as router_metodo_pago

from routers.router_mantenimiento import router as router_mantenimiento

from routers.router_venta import router as router_venta

Base.metadata.create_all(bind=engine)
 
app = FastAPI(

    title="Concesionario de Autos API",

    description="API REST para gestión de concesionario de autos",

    version="1.0.0",

)

app.include_router(router_usuario)

app.include_router(router_cliente)

app.include_router(router_empleado)

app.include_router(router_vehiculo)

app.include_router(router_metodo_pago)

app.include_router(router_mantenimiento)

app.include_router(router_venta)
 
 
@app.get("/")

def root():

    return {"mensaje": "Bienvenido a la API del Concesionario de Autos"}
 
 
if __name__ == "__main__":

    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
 