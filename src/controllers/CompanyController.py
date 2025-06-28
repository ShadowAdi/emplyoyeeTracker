from src.schema import CompanySchema
from sqlmodel import Session,or_,select
from src.models import Company

async def create_company(company:CompanySchema.CompanyCreate,session:Session):
    try:
        statement=select(Company).where(
            or_(
                Company.company_email==company.company_email,
                Company.company_name==company.company_name
            )
        )
        companyFound=session.exec(statement=statement).first()
        if companyFound:
            pass
        
    except:
        pass