from sqlalchemy.orm import Session
from models.productoModel import ProductoModel
from schemas.productoSchema import ProductoSchema

class ProductoService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def obtener_productos(self):
        return self.db.query(ProductoModel).all()

    def obtener_producto_por_id(self, id_producto: int):
        return self.db.query(ProductoModel).filter_by(idProducto=id_producto).first()

    def crear_producto(self, producto: ProductoSchema):
        nuevo_producto = ProductoModel(**producto.dict())
        self.db.add(nuevo_producto)
        self.db.commit()
        self.db.refresh(nuevo_producto)  # Para cargar completamente los datos desde la base de datos
        return nuevo_producto

    def actualizar_producto(self, id_producto: int, producto_actualizado: ProductoSchema):
        producto_existente = self.obtener_producto_por_id(id_producto)
        if producto_existente:
            for key, value in producto_actualizado.dict(exclude_unset=True).items():
                setattr(producto_existente, key, value)
            self.db.commit()
            self.db.refresh(producto_existente)
            return producto_existente
        return None

    def eliminar_producto(self, id_producto: int):
        producto_existente = self.obtener_producto_por_id(id_producto)
        if producto_existente:
            self.db.delete(producto_existente)
            self.db.commit()
            return True
        return False
