from pydantic import BaseModel
import uuid
from datetime import datetime


class UserInputSchema(BaseModel):
    email: str
    password: str


class TokenInput(BaseModel):
    token: str