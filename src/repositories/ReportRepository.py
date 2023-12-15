from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session

from src.configs.database import get_db_connection
from src.models.ReportModel import Report

class ReportRepository:
    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def get_report(self, report: Report) -> Report:
        return self.db.get(
            Report,
            report.id,
        )
    
    def get_all_reports(
        self,
    ) -> List[Report]:
        query = self.db.query(Report)
        return query.all()
    
    def create_report(
        self,
        report: Report
    ):
        if type(report) == dict:
            db_report = Report(**report)
        else:
            db_report = Report(**report.dict())
        self.db.add(db_report)
        self.db.commit()
        self.db.refresh(db_report)
        return db_report