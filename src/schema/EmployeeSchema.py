from pydantic import BaseModel, EmailStr
from typing import List


class EmployeeCreate(BaseModel):
    employee_name: str
    employee_email: EmailStr
    employee_password: str
    role: str
    company_id: int


class EmployeeRead(BaseModel):
    id: int
    employee_name: str
    employee_email: EmailStr
    role: str

    class Config:
        orm_mode = True
