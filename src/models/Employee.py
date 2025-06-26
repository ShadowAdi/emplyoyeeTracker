from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Employee(SQLModel, table=True):
    id: int = Field(default=None, index=True)
    employee_name: str = Field(index=True)
    employee_email: str = Field(index=True)
    employee_password: str = Field(index=True)
    role: str = Field(index=True)
    company_id: Optional[int] = Field(default=None, foreign_key="company.id")


Employee.company = Relationship(back_populates="company.id")
