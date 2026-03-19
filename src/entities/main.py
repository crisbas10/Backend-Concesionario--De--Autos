from src.entities import Base
from src.databases.conexion import engine

Base.metadata.create_all(bind=engine)

print("Tablas creadas correctamente")
