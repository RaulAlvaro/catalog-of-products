from datetime import datetime

from typing import List
from fastapi import Depends
from src.models.ProductModel import Product

from src.repositories.ProductRepository import ProductRepository
from src.repositories.ReportRepository import ReportRepository

from src.schemas.ProductSchema import ProductCreateSchema
from src.schemas.ReportSchema import ReportBase

class ProductService:
    productRepository: ProductRepository
    reportRepository: ReportRepository

    def __init__(
        self, 
        productRepository: ProductRepository = Depends(),
        reportRepository: ReportRepository = Depends()
    ) -> None:
        self.productRepository = productRepository
        self.reportRepository = reportRepository

    def get_product(self, product_id: int) -> Product:
        now = datetime.now()
        current_date = now.strftime("%d/%m/%Y %H:%M:%S")
        self.create_report_of_product({"product_id": product_id, "date": current_date})
        return self.productRepository.get_product(
            Product(id=product_id)
        )
    
    def get_all_products(
        self
    ) -> List[Product]:
        return self.productRepository.get_all_products()
    
    def create_product(
        self,
        product: ProductCreateSchema
    ) -> Product:
        return self.productRepository.create_product(product)
    
    def create_report_of_product(self, report: ReportBase):
        return self.reportRepository.create_report(report)