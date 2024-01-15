from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.productoSchema import ProductoSchema
from services.productoService import ProductoService
from utils.dependencies import get_db

producto_router = APIRouter()

@producto_router.get('/productos', tags=['productos'], response_model=List[ProductoSchema])
def obtener_productos(db: Session = Depends(get_db)) -> List[ProductoSchema]:
    try:
        resultado = ProductoService(db).obtener_productos()
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener productos: {str(e)}")


@producto_router.get('/productos/{id_producto}', tags=['Productos'], response_model=ProductoSchema)
def obtener_producto_por_id(id_producto: int, db: Session = Depends(get_db)) -> ProductoSchema:
    try:
        resultado = ProductoService(db).obtener_producto_por_id(id_producto)
        if resultado:
            return resultado
        else:
            raise HTTPException(status_code=404, detail=f"No se encontró un producto con el ID {id_producto}.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener producto por ID: {str(e)}")

@producto_router.post('/productos', tags=['productos'], response_model=ProductoSchema, status_code=201)
def crear_producto(producto: ProductoSchema, db: Session = Depends(get_db)) -> ProductoSchema:
    try:
        nuevo_producto = ProductoService(db).crear_producto(producto)
        return nuevo_producto
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear producto: {str(e)}")

@producto_router.put('/productos/{id_producto}', tags=['productos'], response_model=ProductoSchema)
def actualizar_producto(id_producto: int, producto_actualizado: ProductoSchema, db: Session = Depends(get_db)) -> ProductoSchema:
    try:
        resultado = ProductoService(db).actualizar_producto(id_producto, producto_actualizado)
        if resultado:
            return resultado
        else:
            raise HTTPException(status_code=404, detail=f"No se encontró un producto con el ID {id_producto}.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar producto: {str(e)}")

@producto_router.delete('/productos/{id_producto}', tags=['productos'], status_code=204)
def eliminar_producto(id_producto: int, db: Session = Depends(get_db)):
    try:
        eliminado_exitosamente = ProductoService(db).eliminar_producto(id_producto)
        if not eliminado_exitosamente:
            raise HTTPException(status_code=404, detail=f"No se encontró un producto con el ID {id_producto}.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar producto: {str(e)}")
