from typing import List, Union

from pydantic import BaseModel

# Product schema
class ProductBase(BaseModel):
    sku: str
    name: str
    price: float
    brand: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

# User schema
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    
    class Config:
        orm_mode = True

# Report schema
class ReportBase(BaseModel):
    date: str
    product_id: int