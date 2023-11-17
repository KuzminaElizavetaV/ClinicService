import datetime

from pydantic import BaseModel, Field


class PetIn(BaseModel):
    name: str = Field(..., title='Pets name', max_length=50)
    birthday: datetime.date = Field(..., title='Pets birthday')
    client_id: int = Field(title='Clients ID')


class Pet(PetIn):
    id: int
