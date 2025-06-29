from pydantic import BaseModel, Field, EmailStr
from typing import List
from .EmployeeSchema import EmployeeRead


from pydantic import BaseModel, EmailStr
from typing import List, Optional
from .EmployeeSchema import EmployeeRead


class CompanyBase(BaseModel):
    company_name: str
    company_email: EmailStr


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
    employees: Optional[List[EmployeeRead]] = []
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
