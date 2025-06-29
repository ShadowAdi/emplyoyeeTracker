from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
class EmployeeBase(BaseModel):
    employee_name: str
    employee_email: EmailStr
    role: str
    createdAt: datetime
    updatedAt: datetime
    address: str
    phoneNumber: str
    timezone: str


class EmployeeCreate(EmployeeBase):
    employee_password: str
    join_code: str

class EmployeeLogin(BaseModel):
    employee_email: str
    employee_password: str

class EmployeeRead(EmployeeBase):
    id: int
    model_config = {"from_attributes": True}
    company_id: int
    company: "CompanyRead"  # forward reference

class EmployeeFull(EmployeeRead):
    company: Optional["CompanyRead"] = []
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


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .CompanySchema import CompanyRead
    from .EmployeeSchema import EmployeeRead
