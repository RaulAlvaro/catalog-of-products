from typing import List

from fastapi import APIRouter, Depends, HTTPException

from src.schemas.ProductSchema import ProductBaseSchema, ProductCreateSchema, ProductSchema
from src.schemas.UserSchema import UserBaseSchema, UserCreateSchema, UserSchema

from typing_extensions import Annotated

from src.services.ProductService import ProductService

from src.utils.auth import get_current_active_user

ProductRouter = APIRouter(tags=["product"])

@ProductRouter.get("/products/")
def get_products(current_user: Annotated[UserBaseSchema, Depends(get_current_active_user)], productService: ProductService = Depends()):
    if current_user:
        return productService.get_all_products()
    raise HTTPException(status_code=400, detail="User not found")

@ProductRouter.get("/products/{product_id}")
def get_product(current_user: Annotated[UserBaseSchema, Depends(get_current_active_user)], product_id: int, productService: ProductService = Depends()):
    if current_user:
        return productService.get_product(product_id)
    raise HTTPException(status_code=400, detail="User not found")

@ProductRouter.post("/products/")
def create_product(current_user: Annotated[UserBaseSchema, Depends(get_current_active_user)], product: ProductCreateSchema, productService: ProductService = Depends()):
    if current_user:
        return productService.create_product(product)
    raise HTTPException(status_code=400, detail="User not found")