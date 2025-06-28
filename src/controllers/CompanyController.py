from src.schema import CompanySchema
from sqlmodel import Session, or_, select
from src.models import Company
from src.config import CustomAuthError, logger
from src.utils import hash_password, verify_password, create_access_token


async def create_company_controller(
    company: CompanySchema.CompanyCreate, session: Session
):
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
        return {
            "success": True,
            "message": "Company Has Been Created",
            "company": db_company,
        }
    except Exception as e:
        logger.error(f"Error Creating Company: {str(e)}")
        raise


async def login_company_controller(
    company: CompanySchema.CompanyLogin, session: Session
):
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

        token = create_access_token(
            data={"sub": str(companyFound["id"]), "email": companyFound["email"]}
        )

        return {
            "message": "Login successful",
            "success": True,
            "company": companyFound,
            "token": token,
            "token_type": "Bearer",
        }
    except Exception as e:
        logger.error(f"Error logging in company: {str(e)}")
        raise


async def get_authenticated_company(session: Session, userId: int):
    try:
        if not userId:
            logger.error(f"UserId Not Found")
            raise CustomAuthError("User Id is Not Given")
        statement = select(Company).where(Company.id == userId)
        companyFound = session.exec(statement=statement).first()
        if not companyFound:
            logger.error(f"Authenticated Company Not Found.")
            raise CustomAuthError(f"Authenticated Company Not Found. {companyFound}")
        logger.info("Authenticated Company Found")
        return {
            "success": True,
            "message": "Authenticated User Found",
            "company": companyFound,
        }

    except Exception as e:
        logger.error(f"Failed to get authenticated Company: {str(userId)}")
        raise
