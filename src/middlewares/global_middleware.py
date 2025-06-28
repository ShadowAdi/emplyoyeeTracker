from fastapi import Request
from starlette.responses import JSONResponse
from src.config import logger
import uuid
import traceback


async def global_exception_handler(req: Request, exc: Exception):
    error_id = str(uuid.uuid4())
    logger.error(f"[{error_id}] Internal error: {traceback.format_exc()}")
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "An Internal Server Error Occurred.",
            "errors": getattr(exc, 'errors', lambda: [])(),
            "error_id": error_id,
        },
    )
