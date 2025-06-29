from sqlmodel import SQLModel, Field, Relationship
from typing import List, TYPE_CHECKING, Optional
from datetime import datetime

if TYPE_CHECKING:
    from .Employee import Employee


class Session(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    start_time: datetime = Field(default_factory=datetime.now,nullable=False)
    end_time: Optional[datetime] = None
    employee_id: int = Field(index=True, foreign_key="employee.id")
    employee: Optional["Employee"] = Relationship(back_populates="sessions")
    note: str | None = Field(index=True, default="")
    createdAt: datetime = Field(default_factory=datetime.now, nullable=False)
    updatedAt: datetime = Field(default_factory=datetime.now, nullable=False)
