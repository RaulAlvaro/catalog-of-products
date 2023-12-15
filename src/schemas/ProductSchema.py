from pydantic import BaseModel


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