from typing import List

from fastapi import APIRouter, Depends

from src.schemas.ProductSchema import ProductBaseSchema, ProductCreateSchema, ProductSchema

from src.services.ProductService import ProductService

ProductRouter = APIRouter(tags=["product"])

@ProductRouter.get("/products/")
def get_products(productService: ProductService = Depends()):
    return productService.get_all_products()

@ProductRouter.get("/products/{product_id}")
def get_product(product_id: int, productService: ProductService = Depends()):
    return productService.get_product(product_id)

@ProductRouter.post("/products/")
def create_product(product: ProductCreateSchema, productService: ProductService = Depends()):
    return productService.create_product(product)