from fastapi import APIRouter, Depends
from src.schema import (
    EmployeeResponse,
    EmployeeCreate,
    EmployeeLogin,
    TokenSentEmployee,
)
from src.controllers import (
    create_employee,
    login_company_controller,
    get_authenticated_employee,
)
from sqlmodel import Session
from src.database import get_session


employeeRouter = APIRouter(prefix="/employee")


@employeeRouter.post("/", response_model=EmployeeResponse)
async def createEmployee(
    employee: EmployeeCreate, session: Session = Depends(get_session)
):
    return await create_employee(employee=employee, session=session)


@employeeRouter.post("/login", response_model=TokenSentEmployee)
async def createEmployee(
    employee: EmployeeLogin, session: Session = Depends(get_session)
):
    return await login_company_controller(employee=employee, session=session)


@employeeRouter.get("/me", response_model=EmployeeResponse)
async def createEmployee(
    employee: EmployeeLogin, session: Session = Depends(get_session)
):
    singleEmployee = await get_authenticated_employee(
        session=session, userId=employee["id"]
    )
    return singleEmployee
