from datetime import datetime
from sqlalchemy import String, Integer, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from .base import Base


class Vehiculo(Base):
    __tablename__ = "vehiculo"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    marca: Mapped[str] = mapped_column(String(50), nullable=False)
    modelo: Mapped[str] = mapped_column(String(50), nullable=False)
    anio: Mapped[int] = mapped_column(Integer, nullable=False)
    precio: Mapped[float] = mapped_column(Float, nullable=False)
    kilometraje: Mapped[int] = mapped_column(Integer, nullable=False)
    estado: Mapped[str] = mapped_column(String(50), nullable=False)
    disponibilidad: Mapped[bool] = mapped_column(Boolean, default=True)

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
