from fastapi import Request
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from src.config import logger

async def http_exception_handler(req: Request, exc: StarletteHTTPException):
    logger.error(f"{exc.detail}")
    return JSONResponse(
        status_code=exc.status_code, content={"success": False, "message": exc.detail}
    )
