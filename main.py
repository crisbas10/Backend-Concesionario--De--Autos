from fastapi import FastAPI
from src.entities import Base
from src.entities.databases.conexion import engine

from routers.routers_usuario import routers as router_usuario
from routers.routers_cliente import routers as router_cliente
from routers.routers_empleado import routers as router_empleado
from routers.routers_vehiculo import routers as router_vehiculo
from routers.routers_metodo_pago import routers as router_metodo_pago
from routers.routers_mantenimiento import routers as router_mantenimiento
from routers.routers_venta import routers as router_venta

# Crear tablas en Neon al iniciar
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Concesionario de Autos API",
    description="API REST para gestión de concesionario de autos",
    version="1.0.0",
)

# Registrar routers
app.include_router(router_usuario)
app.include_router(router_cliente)
app.include_router(router_empleado)
app.include_router(router_vehiculo)
app.include_router(router_metodo_pago)
app.include_router(router_mantenimiento)
app.include_router(router_venta)


@app.get("/")
def root():
    return {"mensaje": "Bienvenido a la API del Concesionario de Autos "}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
