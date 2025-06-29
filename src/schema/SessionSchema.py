from typing import TYPE_CHECKING,Optional
from pydantic import BaseModel
from datetime import datetime


class SessionBase(BaseModel):
    start_time: datetime
    end_time: datetime
    note: str | None

class SessionRead(BaseModel):
    id: int
    createdAt: datetime
    updatedAt: datetime
    model_config = {"from_attributes": True}


class SessionResponse(BaseModel):
    success: bool
    message: Optional[str] = None
    sessions: Optional[SessionRead]


