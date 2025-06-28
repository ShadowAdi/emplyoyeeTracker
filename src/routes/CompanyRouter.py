from fastapi import APIRouter, Depends, HTTPException, status
from src.schema import CompanySchema, EmployeeSchema
from src.models import Company
from sqlmodel import Session, select, or_
from src.database import get_session
from src.utils import hash_password, verify_password
from src.controllers import create_company

comapnyRouter = APIRouter(prefix="/company")


@comapnyRouter.post("/", response_model=CompanySchema.CompanyRead)
async def create_company(
    company: CompanySchema.CompanyCreate, session: Session = Depends(get_session)
):
    return await create_company(company=company, session=session)


@comapnyRouter.post("/login", response_model=CompanySchema.TokenSent)
def login_company(
    company: CompanySchema.CompanyLogin, session: Session = Depends(get_session)
):
    statement = select(Company).where(Company.company_email == company.company_email)
    companyFound = session.exec(statement=statement).first()
    if companyFound is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Company not found"
        )
    if not verify_password(company.password, companyFound.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    return {
        "message": "Login successful",
        "success": True,
        "company_email": companyFound.company_email,
        "company_id": companyFound.id,
    }
