from datetime import datetime
from sqlalchemy import String, Integer, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from .base import Base


class Vehiculo(Base):
    __tablename__ = "vehiculo"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    marca: Mapped[str] = mapped_column(String(50))
    modelo: Mapped[str] = mapped_column(String(50))
    anio: Mapped[int] = mapped_column(Integer)
    precio: Mapped[float] = mapped_column(Float)
    kilometraje: Mapped[int] = mapped_column(Integer)
    estado: Mapped[str] = mapped_column(String(50))
    disponibilidad: Mapped[bool] = mapped_column(Boolean)

    fecha_creacion: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
    fecha_edicion: Mapped[datetime] = mapped_column(DateTime, onupdate=func.now())

    usuario_creacion_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
    usuario_edicion_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
