from pydantic import BaseModel, validator
from datetime import datetime, timezone
from uuid import UUID



class CreateAppoint(BaseModel):

    #user_id: UUID
    #doctor_id: UUID

    user_id: str
    doctor_id: str
    date: datetime


    @validator('date')
    def remove_timezone_info(cls, value):
        return value.replace(tzinfo=None)

