from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base


class Venta(Base):
    __tablename__ = "venta"

    id = Column(Integer, primary_key=True)

    # FOREIGN KEYS
    vendedor_id = Column(Integer, ForeignKey("empleado.id"), nullable=False)
    cliente_id = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    vehiculo_id = Column(Integer, ForeignKey("vehiculo.id"), nullable=False)

    # DATOS
    fecha = Column(DateTime, nullable=False)
    precio_final = Column(Float, nullable=False)
    metodo_pago = Column(String, nullable=False)

    # AUDITORÍA
    fecha_creacion = Column(DateTime, default=func.now(), nullable=False)
    fecha_edicion = Column(DateTime, onupdate=func.now())
    creado_por = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    editado_por = Column(Integer, ForeignKey("usuario.id"))

    # RELACIONES
    vendedor = relationship("Empleado")
    cliente = relationship("Cliente")
    vehiculo = relationship("Vehiculo")
