import datetime

from pydantic import BaseModel, Field, EmailStr, conint


class ClientIn(BaseModel):
    document: str = Field(..., title='Document', max_length=50)
    surname: str = Field(..., title='Surname', max_length=30)
    firstname: str = Field(..., title='First name', max_length=30)
    patronymic: str = Field(..., title='Patronymic', max_length=30)
    birthday: datetime.date = Field(..., title='Birthday')
    phone: int = Field(..., title='Phone number')
    email: EmailStr = Field(..., title='Email', max_length=50)


class Client(ClientIn):
    id: int
