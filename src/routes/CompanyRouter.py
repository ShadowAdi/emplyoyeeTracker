from fastapi import APIRouter, Depends
from src.schema import CompanySchema
from sqlmodel import Session 
from src.database import get_session
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
