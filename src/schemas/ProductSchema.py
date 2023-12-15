from pydantic import BaseModel


class ProductBaseSchema(BaseModel):
    sku: str
    name: str
    price: float
    brand: str

class ProductCreateSchema(ProductBaseSchema):
    pass

class ProductSchema(ProductBaseSchema):
    id: int

    class Config:
        from_attributes = True