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
    
    def get_all_reports(
        self
    ) -> List[Report]:
        return self.reportRepository.get_all_reports()
    
    def create_report(
        self,
        report: ReportBase
    ) -> Report:
        return self.reportRepository.create_report(report)
    