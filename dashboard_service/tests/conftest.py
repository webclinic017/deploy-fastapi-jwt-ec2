from app.main import app
from fastapi import status
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_root_path():
    response = client.get('/')
    assert response.json() == 'First page'
