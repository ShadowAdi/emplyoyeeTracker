from pydantic import BaseModel
from typing import Optional,Any
class ResponseWrapper(BaseModel):
    success: bool
    message: Optional[str] = None
    data: Any = None