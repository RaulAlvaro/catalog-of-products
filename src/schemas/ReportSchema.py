from pydantic import BaseModel

class ReportBase(BaseModel):
    date: str
    product_id: int
