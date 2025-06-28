from src.schema import CompanySchema
from sqlmodel import Session, or_, select
from src.models import Company
from src.config import CustomAuthError, logger
from src.utils import hash_password, verify_password


async def create_company_controller(company: CompanySchema.CompanyCreate, session: Session):
    try:
        statement = select(Company).where(
            Company.company_email == company.company_email,
        )
        companyFound = session.exec(statement=statement).first()
        if companyFound:
            raise CustomAuthError(
                "Company Already Exists with the email. Try To Login!"
            )
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
    except Exception as e:
        logger.error(f"Error Creating Company: {str(e)}")


async def login_company_controller(company: CompanySchema.CompanyLogin, session: Session):
    try:
        statement = select(Company).where(
            Company.company_email == company.company_email
        )
        companyFound = session.exec(statement=statement).first()
        if companyFound is None:
            raise CustomAuthError(
                f"Company don't exist with email {company.company_email}"
            )
        if not verify_password(company.password, companyFound.password):
            raise CustomAuthError("Invalid credentials")

        return {"message": "Login successful", "success": True, "company": companyFound}
    except Exception as e:
        logger.error(f"Error logging in company: {str(e)}")
