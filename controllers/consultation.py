from fastapi import APIRouter, HTTPException
from db import consultations, database
from models.consultation import ConsultationIn, Consultation

router = APIRouter()


@router.get("/consultations/", description='get_all_consultations', operation_id='ConsultationGetAll',
            response_model=list[Consultation])
async def get_consultations():
    query = consultations.select()
    return await database.fetch_all(query)


@router.get("/consultations/{consultation_id}", description='get_consultation', operation_id='ConsultationGet',
            response_model=Consultation)
async def get_consultation(consultation_id: int):
    query = consultations.select().where(consultations.c.id == consultation_id)
    fetch = await database.fetch_one(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Консультация не найдена!')
    return fetch


@router.post("/consultations/", description='add_consultation', operation_id='ConsultationAdd',
             response_model=Consultation)
async def add_consultation(consultation: ConsultationIn):
    query = consultations.insert().values(consultation_date=consultation.consultation_date,
                                          client_id=consultation.client_id,
                                          pet_id=consultation.pet_id,
                                          description=consultation.description)
    last_record_id = await database.execute(query)
    return {**consultation.model_dump(), "id": last_record_id}


@router.put("/consultations/{consultation_id}", description='update_consultation', operation_id='ConsultationUpdate',
            response_model=Consultation)
async def update_consultation(consultation_id: int, new_consultation: ConsultationIn):
    query = consultations.update().where(consultations.c.id == consultation_id).values(**new_consultation.model_dump())
    fetch = await database.execute(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Консультация не найдена!')
    return {**new_consultation.model_dump(), "id": consultation_id}


@router.delete("/consultations/{consultation_id}", description='delete_consultation', operation_id='ConsultationDelete')
async def delete_consultation(consultation_id: int):
    query = consultations.delete().where(consultations.c.id == consultation_id)
    fetch = await database.execute(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Консультация не найдена!')
    return {'message': 'Consultation was deleted'}
