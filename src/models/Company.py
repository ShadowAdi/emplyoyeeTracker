from sqlmodel import Field, SQLModel, Relationship
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .Employee import Employee


class Company(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    company_name: str = Field(index=True)
    company_email: str = Field(index=True)
    company_code: str = Field(index=True, unique=True)
    password: str = Field(index=True)
    employees: List["Employee"] = Relationship(back_populates="company")
