from sqlmodel import SQLModel, Field, Relationship
from typing import Optional,TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from .Company import Company


class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    employee_name: str = Field(index=True)
    employee_email: str = Field(index=True)
    employee_password: str = Field(index=True)
    role: str = Field(index=True)
    company_id: Optional[int] = Field(default=None, foreign_key="company.id")
    company: Optional["Company"] = Relationship(back_populates="employees")
    address: str | None = Field(index=True, default="")
    phoneNumber: str | None = Field(index=True, default="")
    timezone: str = Field(index=True, default="UTC")
    createdAt: datetime = Field(default_factory=datetime.now, nullable=False)
    updatedAt: datetime = Field(default_factory=datetime.now, nullable=False)
