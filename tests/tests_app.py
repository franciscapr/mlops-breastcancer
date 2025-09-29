import os
import json
import pytest
from app.app import create_app
from app.model import ModelService

@pytest.fixture
def client(monkeypatch, tmp_path):

    app = create_app()
    app.testing = True
    return app.test_client()

def test_health(client):
    rv = client.get("/")
    assert rv.status_code == 200
    data = rv.get_json()
    assert "status" in data

def test_predict_invalid_json(client):
    rv = client.post("/predict", data="not-a-json", content_type="application/json")
    assert rv.status_code in (400, 415) or "error" in rv.get_json()


