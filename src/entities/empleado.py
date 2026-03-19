from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Empleado(Base):
    __tablename__ = "empleado"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50))
    telefono: Mapped[str] = mapped_column(String(20))
    correo: Mapped[str] = mapped_column(String(100))
    salario: Mapped[float] = mapped_column(Float)
    cargo: Mapped[str] = mapped_column(String(50))
