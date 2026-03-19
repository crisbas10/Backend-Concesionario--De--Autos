from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Mantenimiento(Base):
    __tablename__ = "mantenimientos"

    # PRIMARY KEY
    id = Column(Integer, primary_key=True, index=True)

    # FOREIGN KEY
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"), nullable=False)

    # DATOS DEL MANTENIMIENTO
    motivo = Column(String, nullable=False)
    fecha = Column(DateTime, nullable=False)
    estado = Column(String, default="Pendiente")

    # AUDITORÍA (OBLIGATORIA)
    fecha_creacion = Column(DateTime, default=func.now(), nullable=False)
    fecha_edicion = Column(DateTime, onupdate=func.now())
    creado_por = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    editado_por = Column(Integer, ForeignKey("usuarios.id"))

    # RELACIÓN
    vehiculo = relationship("Vehiculo")
