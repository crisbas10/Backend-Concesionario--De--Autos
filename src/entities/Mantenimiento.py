from datetime import datetime
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from .base import Base


class Mantenimiento(Base):
    __tablename__ = "mantenimiento"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    vehiculo_id: Mapped[int] = mapped_column(ForeignKey("vehiculo.id"), nullable=False)
    motivo: Mapped[str] = mapped_column(String(200), nullable=False)
    fecha: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    estado: Mapped[str] = mapped_column(String(50), default="Pendiente")

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

    vehiculo = relationship("Vehiculo", foreign_keys=[vehiculo_id])
    usuario_creacion = relationship("Usuario", foreign_keys=[id_usuario_creacion])
    usuario_edita = relationship("Usuario", foreign_keys=[id_usuario_edita])
