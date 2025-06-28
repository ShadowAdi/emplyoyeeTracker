from fastapi import Request
from src.config import CustomAuthError
import uuid
from src.config import logger
import traceback
from starlette.responses import JSONResponse


async def Custom_Auth_Exception_Handler(req: Request, exc: CustomAuthError):
    error_id = str(uuid.uuid4())
    logger.error(f"[{error_id}] Internal error: {traceback.format_exc()}")
    return JSONResponse(
        status_code=401,
        content={
            "success": False,
            "message": exc.message,
            "errors": exc.message,
            "error_id": error_id,
        },
    )
