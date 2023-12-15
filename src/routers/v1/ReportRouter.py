from typing import List

from fastapi import APIRouter, Depends

from src.schemas.ReportSchema import ReportBase

from src.services.ReportService import ReportService

ReportRouter = APIRouter(tags=["report"])

@ReportRouter.get("/reports/")
def get_reports(reportService: ReportService = Depends()):
    return reportService.get_all_reports()

@ReportRouter.get("/reports/{report_id}")
def get_report(report_id: int, reportService: ReportService = Depends()):
    return reportService.get_report(report_id)

@ReportRouter.post("/reports/")
def create_report(report: ReportBase, reportService: ReportService = Depends()):
    return reportService.create_report(report)