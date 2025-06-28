from fastapi import Request
from starlette.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from src.config import logger


async def validation_exception_handler(req: Request, exc: RequestValidationError):
    logger.error(f"Validation Failed {exc.errors()}")
    return JSONResponse(
        status_code=522,
        content={
            "success": False,
            "messsage": "Validation Failed.",
            "errors": exc.errors(),
        },
    )
