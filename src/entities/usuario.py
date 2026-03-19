from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre_usuario: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    correo: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    rol: Mapped[str] = mapped_column(String(20), default="vendedor")
