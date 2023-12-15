from typing import List

from fastapi import APIRouter, Depends

from src.schemas.ReportSchema import ReportBase, Report

from src.services.ReportService import ReportService

ReportRouter = APIRouter(tags=["report"])

@ReportRouter.get("/reports/", response_model=List[Report])
def get_reports(reportService: ReportService = Depends()):
    return reportService.get_all_reports()

@ReportRouter.get("/reports/{report_id}", response_model=Report)
def get_report(report_id: int, reportService: ReportService = Depends()):
    return reportService.get_report(report_id)

@ReportRouter.get("/reports/product/{product_id}", response_model=List[Report])
def get_reports_by_product_id(product_id: int, reportService: ReportService = Depends()):
    return reportService.get_reports_by_product_id(product_id)

@ReportRouter.post("/reports/", response_model=Report)
def create_report(report: ReportBase, reportService: ReportService = Depends()):
    return reportService.create_report(report)