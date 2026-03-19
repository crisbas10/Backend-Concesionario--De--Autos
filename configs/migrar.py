from src.entities.databases.conexion import engine
from src.entities.base import Base


from src.entities.usuario import Usuario
from src.entities.cliente import Cliente
from src.entities.empleado import Empleado
from src.entities.vehiculo import Vehiculo
from src.entities.venta import Venta
from src.entities.Mantenimiento import Mantenimiento

Base.metadata.create_all(bind=engine)

print("✅ Tablas creadas correctamente")
