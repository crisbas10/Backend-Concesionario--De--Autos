#aqui van las clases antiguas
# vehiculo, mantemiento, cliente, empleado, venta, etc.
# lo que importa es que vayan las clases del modelo de negocio y la clase Usuario junto con las que se menciono en el 
#mensaje de whatsapp y del documento del profesor


from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func

#importante correr pip install -r requerements.txt para instalar las dependencias necesarias, como SQLAlchemy y python-dotenv, para que el código funcione correctamente.

# Esta es la Clase Base de la que heredarán todas tus entidades
"""es una clase que proviene directamente de la librería SQLAlchemy, específicamente del módulo ORM (Object-Relational Mapper)."""
class Base(DeclarativeBase): 
    pass

# Entidad Usuario (Requisito obligatorio del proyecto)
 
class Usuario(Base):
    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre_usuario: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    correo: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    rol: Mapped[str] = mapped_column(String(20), default="vendedor") # admin o vendedor

    def __repr__(self) -> str:
        return f"<Usuario(id={self.id}, nombre='{self.nombre_usuario}')>"


class Empleado():
    def __init__(self, nombre, telefono, correo, salario, cargo):
        super().__init__(
            nombre, telefono, correo
        )  # invoca al constructor de la clase padre (Persona)
        self.salario = salario
        self.cargo = cargo

class Empleado():
    def __init__(self, nombre, telefono, correo, salario, cargo):
        super().__init__(
            nombre, telefono, correo
        )  # invoca al constructor de la clase padre (Persona)
        self.salario = salario
        self.cargo = cargo

class Vehiculo():
    def __init__(
        self,
        ID: int,
        Marca: str,
        Modelo: str,
        Año: int,
        Precio: float,
        Kilometraje: int,
        Estado: str,
        Disponibilidad: bool,
    ):
        self.ID = ID
        self.Marca = Marca
        self.Modelo = Modelo
        self.Año = Año
        self.Precio = Precio
        self.Kilometraje = Kilometraje
        self.Estado = Estado
        self.Disponibilidad = Disponibilidad


