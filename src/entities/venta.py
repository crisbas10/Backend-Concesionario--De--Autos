from datetime import datetime
from sqlalchemy import Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from .base import Base


class Venta(Base):
    __tablename__ = "venta"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    empleado_id: Mapped[int] = mapped_column(ForeignKey("empleado.id"), nullable=False)
    cliente_id: Mapped[int] = mapped_column(ForeignKey("cliente.id"), nullable=False)
    vehiculo_id: Mapped[int] = mapped_column(ForeignKey("vehiculo.id"), nullable=False)
    metodo_pago_id: Mapped[int] = mapped_column(ForeignKey("metodo_pago.id"), nullable=False)

    fecha: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    precio_final: Mapped[float] = mapped_column(Float, nullable=False)

    fecha_creacion: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    fecha_edicion: Mapped[datetime] = mapped_column(DateTime, onupdate=func.now(), nullable=True)
    id_usuario_creacion: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
    id_usuario_edita: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=True)

    empleado = relationship("Empleado", foreign_keys=[empleado_id])
    cliente = relationship("Cliente", foreign_keys=[cliente_id])
    vehiculo = relationship("Vehiculo", foreign_keys=[vehiculo_id])
    metodo_pago = relationship("MetodoPago", foreign_keys=[metodo_pago_id])
    usuario_creacion = relationship("Usuario", foreign_keys=[id_usuario_creacion])
    usuario_edita = relationship("Usuario", foreign_keys=[id_usuario_edita])
