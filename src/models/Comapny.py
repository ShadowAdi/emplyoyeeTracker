from sqlmodel import Field, SQLModel, Relationship
from typing import List


class Company(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    company_name: str = Field(index=True)
    company_email: str = Field(index=True)
    password: str = Field(index=True)
    employees: List[int] = Relationship(back_populates="company")
