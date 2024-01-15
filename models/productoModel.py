from sqlalchemy import Column, Integer, String, DateTime, func, Numeric
from sqlalchemy.orm import relationship
from config.database import Base

# Realiza el modelo de la tabla de la base de datos que va a representar
class ProductoModel(Base):
    __tablename__ = 'productos'

    idProducto = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(100), nullable=False)
    precio = Column(Numeric(precision=10, scale=2), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
