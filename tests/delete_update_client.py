import pytest
from fastapi.testclient import TestClient
from main import app


def test_delete_client(test_db):
    """Тест удаления клиента"""
    client_data = {  # Создание клиента для удаления
        "document": "7000 698521",
        "surname": "Анин",
        "firstname": "Иван",
        "patronymic": "Петрович",
        "birthday": "1976-01-01",
        "phone": "89026951452",
        "email": "ivan@mail.ru",
    }
    with TestClient(app) as client:
        response = client.post("/clients/", json=client_data)
    assert response.status_code == 200
    client_id = response.json()["id"]

    with TestClient(app) as client:  # Удаление клиента
        response = client.delete(f"/clients/{client_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Client deleted"}

    with TestClient(app) as client:  # Проверка, что клиента больше нет
        response = client.get(f"/clients/{client_id}")
    assert response.status_code == 404


def test_update_client(test_db):
    """Тест обновления клиента """
    client_data = {  # Создание клиента для обновления
        "document": "7002 698521",
        "surname": "Петров",
        "firstname": "Иван",
        "patronymic": "Петрович",
        "birthday": "1976-01-01",
        "phone": "89026951452",
        "email": "ivan@mail.ru",
    }
    with TestClient(app) as client:
        response = client.post("/clients/", json=client_data)
    assert response.status_code == 200
    client_id = response.json()["id"]

    update_client_data = {  # Обновленные данные клиента
        "document": "7003 698521",
        "surname": "Мишин",
        "firstname": "Иван",
        "patronymic": "Петрович",
        "birthday": "1986-01-01",
        "phone": "89026951452",
        "email": "ivan@mail.ru",
    }
    with TestClient(app) as client:
        response = client.put(f"/clients/{client_id}", json=update_client_data)
    assert response.status_code == 200
    assert response.json() == {**update_client_data, "id": client_id}


if __name__ == '__main__':
    pytest.main(['-v'])
