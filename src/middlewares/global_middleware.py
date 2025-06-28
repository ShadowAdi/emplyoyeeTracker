from fastapi import Request
from starlette.responses import JSONResponse
from src.config import logger


async def global_exception_handler(req: Request, exc: Exception):
    logger.error(f"Internal Server Error Occurred {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "An Internal Server Error Occurred.",
            "detail": str(exc),
        },
    )

