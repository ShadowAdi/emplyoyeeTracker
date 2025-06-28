from fastapi import Request
from starlette.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from src.config import logger
import uuid


async def validation_exception_handler(req: Request, exc: RequestValidationError):
    error_id = str(uuid.uuid4())
    logger.error(f"Validation Failed {exc.errors()}")
    return JSONResponse(
        status_code=522,
        content={
            "success": False,
            "messsage": "Validation Failed Error.",
            "errors": exc.errors(),
            "error_id": error_id,
        },
    )
