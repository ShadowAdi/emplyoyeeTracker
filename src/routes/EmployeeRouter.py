from fastapi import APIRouter, Depends
from src.schema import (
    EmployeeResponse,
    EmployeeCreate,
    EmployeeLogin,
    TokenSentEmployee,
)
from src.controllers import create_employee, get_authenticated_employee, login_employee
from sqlmodel import Session
from src.database import get_session
from src.dependency import get_current_employee


employeeRouter = APIRouter(prefix="/employee")


@employeeRouter.post("/", response_model=EmployeeResponse)
async def createEmployee(
    employee: EmployeeCreate, session: Session = Depends(get_session)
):
    return await create_employee(employee=employee, session=session)


@employeeRouter.post("/login", response_model=TokenSentEmployee)
async def loginEmployee(
    employee: EmployeeLogin, session: Session = Depends(get_session)
):
    return await login_employee(employee=employee, session=session)


@employeeRouter.get("/me", response_model=EmployeeResponse)
async def authenticatedEmployee(
    session: Session = Depends(get_session), employee=Depends(get_current_employee)
):
    singleEmployee = await get_authenticated_employee(
        session=session, userId=employee["id"]
    )
    return singleEmployee
