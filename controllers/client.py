from fastapi import APIRouter, HTTPException
from db import clients, database
from models.client import ClientIn, Client

router = APIRouter()


@router.get("/clients/", response_model=list[Client])
async def get_clients():
    query = clients.select()
    return await database.fetch_all(query)


@router.get("/clients/{client_id}", response_model=Client)
async def get_client(client_id: int):
    query = clients.select().where(clients.c.id == client_id)
    fetch = await database.fetch_one(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Клиент не найден!')
    return fetch


@router.post("/clients/", response_model=Client)
async def add_client(client: ClientIn):
    query = clients.insert().values(document=client.document,
                                    surname=client.surname,
                                    firstname=client.firstname,
                                    patronymic=client.patronymic,
                                    birthday=client.birthday,
                                    phone=client.phone,
                                    email=client.email)
    last_record_id = await database.execute(query)
    return {**client.model_dump(), "id": last_record_id}


@router.put("/clients/{client_id}", response_model=Client)
async def update_client(client_id: int, new_client: ClientIn):
    query = clients.update().where(clients.c.id == client_id).values(**new_client.model_dump())
    fetch = await database.execute(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Клиент не найден')
    return {**new_client.model_dump(), "id": client_id}


@router.delete("/clients/{client_id}")
async def delete_client(client_id: int):
    query = clients.delete().where(clients.c.id == client_id)
    fetch = await database.execute(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Клиент не найден')
    return {'message': 'Client deleted'}
