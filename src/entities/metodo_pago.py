from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class MetodoPago(Base):
    __tablename__ = "metodo_pago"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tipo: Mapped[str] = mapped_column(String(50))
