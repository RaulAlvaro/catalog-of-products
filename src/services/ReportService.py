from datetime import datetime
from typing import List
from fastapi import Depends
from src.models.ReportModel import Report
from src.repositories.ReportRepository import ReportRepository
from src.schemas.ReportSchema import ReportBase

class ReportService:
    reportRepository: ReportRepository

    def __init__(
        self, reportRepository: ReportRepository = Depends()
    ) -> None:
        self.reportRepository = reportRepository

    def get_report(self, report_id: int) -> Report:
        return self.reportRepository.get_report(
            Report(id=report_id)
        )
    
    def get_reports_by_product_id(self, product_id: int) -> List[Report]:
        return self.reportRepository.get_reports_by_product_id(
            Report(product_id=product_id)
        )
    
    def get_all_reports(
        self
    ) -> List[Report]:
        return self.reportRepository.get_all_reports()
    
    def create_report(
        self,
        report: ReportBase
    ) -> Report:
        now = datetime.now()
        current_date = now.strftime("%d/%m/%Y %H:%M:%S")
        return self.reportRepository.create_report({ "product_id": report.product_id, "date": current_date })
    