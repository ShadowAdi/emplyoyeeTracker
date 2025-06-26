from pydantic import BaseModel, Field, EmailStr
from typing import List
from .EmployeeSchema import EmployeeRead


class CompanyCreate(BaseModel):
    company_name: str
    company_email: EmailStr
    password: str


class CompanyLogin:
    company_email: EmailStr
    password: str



class CompanyRead(BaseModel):
    id: int
    company_name: str
    company_email: EmailStr

    class Config:
        orm_mode = True


class CompanyWithEmployees(BaseModel):
    employees: List[EmployeeRead] = []


class TokenSent:
    company:CompanyRead
    token:str