from fastapi import Request
from starlette.responses import JSONResponse
from fastapi.exceptions import ResponseValidationError
from src.config import logger
import uuid
import uuid
import traceback


async def response_validation_error(req: Request, exc: ResponseValidationError):
    error_id = str(uuid.uuid4())
    logger.error(
        f"[{error_id}] RESPONSE VALIDATION FAILED. The Response Sent by you does not match. {traceback.format_exc()}"
    )
    return JSONResponse(
        status_code=500,
        content={
            "success": True,
            "message": f"Response Validation Failed: {traceback.format_exc()}",
            "errors": exc.errors(),
            "error_id": error_id,
        },
    )
