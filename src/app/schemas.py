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
        from_attributes = True

# User schema
class UserBase(BaseModel):
    username: str
    email: str
    

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id: int
    hashed_password: str
    is_active: bool
    
    class Config:
        from_attributes = True

# Report schema
class ReportBase(BaseModel):
    date: str
    product_id: int


# Token schema
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None