from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session

from src.configs.database import get_db_connection
from src.models.ProductModel import Product
from src.models.ReportModel import Report

class ProductRepository:
    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def get_product(self, product: Product) -> Product:
        return self.db.get(
            Product,
            product.id,
        )
    
    def get_all_products(
        self,
    ) -> List[Product]:
        query = self.db.query(Product)
        return query.all()
    
    def create_product(
        self,
        product: Product
    ):
        db_product = Product(**product.dict())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product