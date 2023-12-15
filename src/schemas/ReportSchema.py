from pydantic import BaseModel

class ReportBase(BaseModel):
    product_id: int

class Report(ReportBase):
    pass
    date: str