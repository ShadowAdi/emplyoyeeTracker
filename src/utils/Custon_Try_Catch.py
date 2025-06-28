from functools import wraps
from pydantic import BaseModel
import traceback
from typing import Optional, Type, Callable
from src.schema import ResponseWrapper
from src.config import logger


def handle_exceptions(
    success_message: Optional[str],
    response_model: Optional[Type[BaseModel]] = None,
):
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                result = await func(*args, **kwargs)
                data = (
                    response_model.model_validate(result) if response_model else result
                )
                return ResponseWrapper(success=True, message=success_message, data=data)
            except Exception as e:
                logger.error(f"INTERNAL SERVER ERROR {traceback.print_exc()}")
                traceback.print_exc()
                return ResponseWrapper(success=False, message=str(e), data=None)

        return wrapper

    return decorator
