from src.schema import CompanySchema
from sqlmodel import Session, or_, select
from src.models import Company
from src.config import CustomAuthError
from src.utils import hash_password


async def create_company(company: CompanySchema.CompanyCreate, session: Session):
    try:
        statement = select(Company).where(
            Company.company_email == company.company_email,
        )
        companyFound = session.exec(statement=statement).first()
        if companyFound:
            CustomAuthError("Company Already Exists with the email. Try To Login!")
        hashed_pw = hash_password(company.password)
        db_company = Company(
            company_email=company.company_email,
            company_name=company.company_name,
            password=hashed_pw,
        )
        session.add(db_company)
        session.commit()
        session.refresh(db_company)
        return db_company
    except:
        pass
