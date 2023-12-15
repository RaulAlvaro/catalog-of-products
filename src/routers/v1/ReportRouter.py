from typing import List

from fastapi import APIRouter, Depends, HTTPException

from src.schemas.ReportSchema import ReportBase, Report

from src.schemas.UserSchema import UserBaseSchema, UserCreateSchema, UserSchema

from typing_extensions import Annotated

from src.services.ReportService import ReportService

from src.utils.auth import get_current_active_user

ReportRouter = APIRouter(tags=["report"])

@ReportRouter.get("/reports/", response_model=List[Report])
def get_reports(current_user: Annotated[UserBaseSchema, Depends(get_current_active_user)], reportService: ReportService = Depends()):
    if current_user:
        return reportService.get_all_reports()
    raise HTTPException(status_code=400, detail="User not found")

@ReportRouter.get("/reports/{report_id}", response_model=Report)
def get_report(current_user: Annotated[UserBaseSchema, Depends(get_current_active_user)], report_id: int, reportService: ReportService = Depends()):
    if current_user:
        return reportService.get_report(report_id)
    raise HTTPException(status_code=400, detail="User not found")

@ReportRouter.get("/reports/product/{product_id}", response_model=List[Report])
def get_reports_by_product_id(current_user: Annotated[UserBaseSchema, Depends(get_current_active_user)], product_id: int, reportService: ReportService = Depends()):
    if current_user:
        return reportService.get_reports_by_product_id(product_id)
    raise HTTPException(status_code=400, detail="User not found")

@ReportRouter.post("/reports/", response_model=Report)
def create_report(current_user: Annotated[UserBaseSchema, Depends(get_current_active_user)], report: ReportBase, reportService: ReportService = Depends()):
    if current_user:
        return reportService.create_report(report)
    raise HTTPException(status_code=400, detail="User not found")
