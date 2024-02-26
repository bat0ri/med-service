from pydantic import BaseModel


class CardInput(BaseModel):
    name: str