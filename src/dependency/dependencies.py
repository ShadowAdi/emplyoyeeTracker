from sqlmodel import Session, select
from fastapi import Depends
from src.models import Company
from src.utils import decode_access_token, oauth2scheme
from src.config import CustomAuthError, logger
from src.database import get_session


def get_current_company(
    token: str = Depends(oauth2scheme), db: Session = Depends(get_session)
):
    payload = decode_access_token(token=token)
    if not payload:
        logger.error(f"Failed to get the payload")
        raise CustomAuthError("INTERNAL SERVER ERROR. Failed to get the payload")
    user_id_str = payload.get("sub")
    user_id = int(user_id_str) if user_id_str else None

    if not user_id:
        logger.error(
            f"INTERNAL SERVER ERROR. User Id does not exist in payload: {payload}"
        )
        raise CustomAuthError("INTERNAL SERVER ERROR. User Id Do Not Exist In Payload")

    statement = select(Company).where(Company.id == user_id)
    company_found = db.exec(statement).first()

    if not company_found:
        logger.error(f"Company not found for user_id: {user_id}")
        raise CustomAuthError("Company not found")
    return company_found
