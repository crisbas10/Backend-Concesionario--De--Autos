from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base


class Mantenimiento(Base):
    __tablename__ = "mantenimiento"

    id = Column(Integer, primary_key=True)

    vehiculo_id = Column(Integer, ForeignKey("vehiculo.id"), nullable=False)

    motivo = Column(String, nullable=False)
    fecha = Column(DateTime, nullable=False)
    estado = Column(String, default="Pendiente")

    # auditoría
    fecha_creacion = Column(DateTime, default=func.now(), nullable=False)
    fecha_edicion = Column(DateTime, onupdate=func.now())
    creado_por = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    editado_por = Column(Integer, ForeignKey("usuario.id"))

    vehiculo = relationship("Vehiculo")
