from .CompanySchema import (
    CompanyCreate,
    CompanyBase,
    CompanyFull,
    CompanyLogin,
    CompanyResponse,
    CompanyRead
)
from .EmployeeSchema import (
    EmployeeCreate,
    EmployeeBase,
    EmployeeFull,
    EmployeeLogin,
    EmployeeResponse,
    TokenSentEmployee,
    EmployeeRead,
)

CompanyRead.model_rebuild()
CompanyFull.model_rebuild()
EmployeeRead.model_rebuild()
EmployeeFull.model_rebuild()
