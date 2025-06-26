from fastapi import APIRouter, Depends
from src.schema import CompanySchema, EmployeeSchema
from src.models import Company
from sqlmodel import Session
from src.database import get_session

comapnyRouter = APIRouter(prefix="/company")


@comapnyRouter.post("/", response_model=CompanySchema.CompanyRead)
def create_company(
    company: CompanySchema.CompanyCreate, session: Session = Depends(get_session)
):
    db_company = Company(**company.model_dump())
    session.add(db_company)
    session.commit()
    session.refresh(db_company)
    return db_company
