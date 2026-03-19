from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from .base import Base


class Cliente(Base):
    __tablename__ = "cliente"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    telefono: Mapped[str] = mapped_column(String(20), nullable=True)
    correo: Mapped[str] = mapped_column(String(100), nullable=True)

    # Auditoría
    fecha_creacion: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
    fecha_edicion: Mapped[datetime] = mapped_column(
        DateTime, onupdate=func.now(), nullable=True
    )
    id_usuario_creacion: Mapped[int] = mapped_column(
        ForeignKey("usuario.id"), nullable=False
    )
    id_usuario_edita: Mapped[int] = mapped_column(
        ForeignKey("usuario.id"), nullable=True
    )

    usuario_creacion = relationship("Usuario", foreign_keys=[id_usuario_creacion])
    usuario_edita = relationship("Usuario", foreign_keys=[id_usuario_edita])
