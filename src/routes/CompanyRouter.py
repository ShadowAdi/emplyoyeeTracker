from fastapi import APIRouter, Depends, HTTPException, status
from src.schema import CompanySchema, EmployeeSchema
from src.models import Company
from sqlmodel import Session, select, or_
from src.database import get_session
from src.utils import hash_password, verify_password
from src.controllers import create_company, login_company

comapnyRouter = APIRouter(prefix="/company")


@comapnyRouter.post("/", response_model=CompanySchema.CompanyRead)
async def create_company(
    company: CompanySchema.CompanyCreate, session: Session = Depends(get_session)
):
    return await create_company(company=company, session=session)


@comapnyRouter.post("/login", response_model=CompanySchema.TokenSent)
async def login_company(
    company: CompanySchema.CompanyLogin, session: Session = Depends(get_session)
):
    return await login_company(company=company, session=session)
