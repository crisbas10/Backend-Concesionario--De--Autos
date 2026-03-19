from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Venta(Base):
    __tablename__ = "ventas"

    # PRIMARY KEY
    id = Column(Integer, primary_key=True, index=True)

    # FOREIGN KEYS (RELACIONES)
    vendedor_id = Column(Integer, ForeignKey("vendedores.id"), nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"), nullable=False)

    # DATOS DE LA VENTA
    fecha = Column(DateTime, nullable=False)
    precio_final = Column(Float, nullable=False)
    metodo_pago = Column(String, nullable=False)

    # AUDITORÍA (OBLIGATORIA)
    fecha_creacion = Column(DateTime, default=func.now(), nullable=False)
    fecha_edicion = Column(DateTime, onupdate=func.now())
    creado_por = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    editado_por = Column(Integer, ForeignKey("usuarios.id"))

    # RELACIONES (OPCIONAL PERO PRO)
    vendedor = relationship("Vendedor")
    cliente = relationship("Cliente")
    vehiculo = relationship("Vehiculo")
