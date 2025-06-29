from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime


class CompanyBase(BaseModel):
    company_name: str
    company_email: EmailStr
    createdAt: datetime
    updatedAt: datetime
    address: str
    companyLogo: str
    phoneNumber: str
    timezone: str


class CompanyCreate(CompanyBase):
    password: str


class CompanyLogin(BaseModel):
    company_email: EmailStr
    password: str


class CompanyRead(CompanyBase):
    id: int
    company_code: str
    model_config = {"from_attributes": True}


class CompanyFull(CompanyRead):
    employees: Optional[List["EmployeeRead"]] = []  # forward reference
    model_config = {"from_attributes": True}


class TokenSent(BaseModel):
    message: str
    success: bool
    company: CompanyRead
    token: str
    token_type: str


class CompanyResponse(BaseModel):
    success: bool
    message: Optional[str] = None
    company: CompanyRead


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .CompanySchema import CompanyRead
    from .EmployeeSchema import EmployeeRead
