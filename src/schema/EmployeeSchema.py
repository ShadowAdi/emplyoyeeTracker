from pydantic import BaseModel, EmailStr
from typing import List,Optional
from .CompanySchema import CompanyRead


class EmployeeBase(BaseModel):
    employee_name: str
    employee_email: EmailStr
    role: str


class EmployeeCreate(EmployeeBase):
    employee_password: str


class EmployeeLogin(BaseModel):
    employee_email: str
    employee_password: str


class EmployeeRead(EmployeeBase):
    id: int
    model_config = {"from_attributes": True}
    company_id: int
    company: CompanyRead

class EmployeeFull(EmployeeRead):
    company: Optional[CompanyRead] = []
    model_config = {"from_attributes": True}



class TokenSentEmployee(BaseModel):
    message: str
    success: bool
    employee: EmployeeRead
    token: str
    token_type: str

class EmployeeResponse(BaseModel):
    success: bool
    message: Optional[str] = None
    employee: EmployeeRead