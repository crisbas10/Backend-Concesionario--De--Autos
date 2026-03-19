from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Cliente(Base):
    __tablename__ = "cliente"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50))
    telefono: Mapped[str] = mapped_column(String(20))
    correo: Mapped[str] = mapped_column(String(100))
