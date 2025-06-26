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

    model_config = {
        "from_attributes": True  # 👈 Enables ORM support in Pydantic v2
    }


class CompanyWithEmployees(BaseModel):
    employees: List[EmployeeRead] = []


class TokenSent(BaseModel):
    message: str
    success: bool
    company_email: str
    company_id:int 