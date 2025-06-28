from fastapi import APIRouter, Depends
from src.schema import CompanySchema
from sqlmodel import Session
from src.database import get_session
from src.controllers import (
    create_company_controller,
    login_company_controller,
    get_authenticated_company,
)
from src.dependency import get_current_company

comapnyRouter = APIRouter(prefix="/company")


@comapnyRouter.post("/", response_model=CompanySchema.CompanyResponse)
async def create_company(
    company: CompanySchema.CompanyCreate, session: Session = Depends(get_session)
):
    return await create_company_controller(company=company, session=session)


@comapnyRouter.post("/login", response_model=CompanySchema.TokenSent)
async def login_company(
    company: CompanySchema.CompanyLogin, session: Session = Depends(get_session)
):
    return await login_company_controller(company=company, session=session)


@comapnyRouter.get("/me", response_model=CompanySchema.CompanyResponse)
async def authenticated_company(
    session: Session = Depends(get_session), company=Depends(get_current_company)
):
    singleCompany = await get_authenticated_company(
        session=session, userId=company["id"]
    )
    return singleCompany
