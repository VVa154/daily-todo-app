# tests/test_app.py
from app import add_numbers, app

def test_add_numbers():
    assert add_numbers(2, 3) == 5

def test_add_and_get_todo():
    client = app.test_client()
    response = client.post("/todos", json={"task": "Buy milk"})
    assert response.status_code == 201
    response = client.get("/todos")
    data = response.get_json()
    assert "Buy milk" in [t["task"] for t in data["todos"]]

def test_mark_done():
    client = app.test_client()
    client.post("/todos", json={"task": "Walk dog"})
    response = client.post("/todos/0/done")
    assert response.status_code == 200
    response = client.get("/todos")
    data = response.get_json()
    assert data["todos"][0]["done"] == True
