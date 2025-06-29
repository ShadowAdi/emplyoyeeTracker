from src.schema import EmployeeCreate, EmployeeLogin
from sqlmodel import Session, select, or_
from src.models import Employee, Company
from src.config import CustomAuthError, logger
from src.utils import hash_password, verify_password, create_access_token
from sqlalchemy import func

async def create_employee(employee: EmployeeCreate, session: Session):
    try:
        companyExist = session.exec(
            select(Company).where(func.lower(Company.company_code) == employee.join_code.lower())
        ).first()
        if not companyExist:
            raise CustomAuthError("Company Do Not Exist. Is Joining Code Correct")
        statement = select(Employee).where(
            Employee.employee_email == employee.employee_email
        )
        employeeFound = session.exec(statement=statement).first()
        if employeeFound:
            raise CustomAuthError(
                "Employee With Same Mail Already Exists. Try To Login!"
            )
        hashed_pw = hash_password(employee.employee_password)
        db_employee = Employee(
            employee_password=hashed_pw,
            employee_email=employee.employee_email,
            employee_name=employee.employee_name,
            role=employee.role,
            company_id=companyExist.id,
        )
        session.add(db_employee)
        session.commit()
        session.refresh(db_employee)
        return {
            "success": True,
            "message": "Employee Has Been Created",
            "employee": db_employee,
        }
    except Exception as e:
        logger.error(f"Error Creating Employee: {str(e)}")
        raise


async def login_employee(employee: EmployeeLogin, session: Session):
    try:
        statement = select(Employee).where(
            Employee.employee_email == employee.employee_email
        )
        employeeFound = session.exec(statement=statement).first()
        if employeeFound is None:
            raise CustomAuthError(
                f"Employee With  Mail: {employee.employee_email} Don't Exists. Try to signup"
            )
        if not verify_password(
            employee.employee_password, employeeFound.employee_password
        ):
            raise CustomAuthError("Invalid credentials")

        token = create_access_token(
            data={"sub": str(employeeFound.id), "email": employeeFound.employee_email}
        )
        return {
            "success": True,
            "message": "Login Successfull",
            "employee": employeeFound,
            "token": token,
            "token_type": "Bearer",
        }

    except Exception as e:
        logger.error(f"Error login Employee: {str(e)}")
        raise


async def get_authenticated_employee(session: Session, userId: int):
    if not userId:
        logger.error(f"UserId Not Found")
        raise CustomAuthError("User Id is Not Given")
    try:
        statement = select(Employee).where(Employee.id == userId)
        employeeFound = session.exec(statement=statement).first()
        if not employeeFound:
            logger.error(f"Authenticated Employee Not Found.")
            raise CustomAuthError(f"Authenticated Employee Not Found. {employeeFound}")
        logger.info("Authenticated Employee Found")
        return {
            "success": True,
            "message": "Authenticated User Found",
            "employee": employeeFound,
        }
    except Exception as e:
        logger.error(f"Failed to get authenticated employee: {str(userId)}")
        raise
