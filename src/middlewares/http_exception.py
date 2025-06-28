from fastapi import Request
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from src.config import logger
import uuid


async def http_exception_handler(req: Request, exc: StarletteHTTPException):
    error_id = str(uuid.uuid4())
    logger.error(f"{exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail,
            "errors": exc.errors(),
            "error_id": error_id,
        },
    )
