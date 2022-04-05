from fastapi.testclient import TestClient

from coalesce.api import api

client = TestClient(api)


def test_missing_member_id():
    response = client.get("/")
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "value_error.missing"


def test_unsupported_strategy():
    params = {
        "member_id": 1,
        "strategy": "yolo"
    }
    response = client.get("/", params=params)
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "type_error.enum"


def test_invalid_coverage_data():
    params = {
        "member_id": 3,
    }
    response = client.get("/", params=params)
    assert response.status_code == 424
    assert response.json()["detail"] == "Upstream data is malformed"


def test_invalid_member_id():
    params = {
        "member_id": 100,
    }
    response = client.get("/", params=params)
    assert response.status_code == 424
    assert response.json()["detail"] == "Failed to get upstream data"


def test_average_member1():
    params = {
        "member_id": 1,
        "strategy": "average"
    }
    response = client.get("/", params=params)
    assert response.status_code == 200
    assert response.json() == {"deductible": 100, "stop_loss": 167, "oop_max": 233}


def test_minimum_member1():
    params = {
        "member_id": 2,
        "strategy": "minimum"
    }
    response = client.get("/", params=params)
    assert response.status_code == 200
    assert response.json() == {"deductible": 100, "stop_loss": 200, "oop_max": 200}


def test_maximum_member1():
    params = {
        "member_id": 2,
        "strategy": "maximum"
    }
    response = client.get("/", params=params)
    assert response.status_code == 200
    assert response.json() == {"deductible": 400, "stop_loss": 500, "oop_max": 600}
