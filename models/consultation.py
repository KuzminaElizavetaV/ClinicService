import datetime

from pydantic import BaseModel, Field


class ConsultationIn(BaseModel):
    consultation_date: datetime.date = Field(..., title='Consultations day')
    client_id: int = Field(title='Clients ID')
    pet_id: int = Field(title='Pets ID')
    description: str = Field(default='', title="Description", max_length=300)


class Consultation(ConsultationIn):
    id: int
