from pydantic import BaseModel, Field, EmailStr
from typing import List
from .EmployeeSchema import EmployeeRead


class CompanyCreate(BaseModel):
    company_name: str
    company_email: EmailStr
    password: str


class CompanyLogin(BaseModel):
    company_email: EmailStr
    password: str


class CompanyRead(BaseModel):
    id: int
    company_name: str
    company_email: EmailStr

    model_config = {"from_attributes": True}


class CompanyWithEmployees(BaseModel):
    employees: List[EmployeeRead] = []


class TokenSent(BaseModel):
    message: str
    success: bool
    company: CompanyRead
    token: str
    token_type: str
