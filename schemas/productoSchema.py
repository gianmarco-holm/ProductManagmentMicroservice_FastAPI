from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProductoSchema(BaseModel):
    idProducto: Optional[int] = Field(None, description="ID del producto (opcional)")
    nombre: str = Field(..., description="Nombre del producto")
    descripcion: str = Field(..., description="Descripción del producto")
    precio: float = Field(..., gt=0, description="Precio del producto")
    created_at: Optional[datetime] = Field(None, description="Fecha de creación del producto")

    class Config:
        title = "Esquema de Producto"
        description = "Modelo para representar un producto"
        json_schema_extra = {
            "examples": [
                {
                    "nombre": "Producto1",
                    "descripcion": "Descripción del producto 1",
                    "precio": 19.99
                }
            ]
        }
