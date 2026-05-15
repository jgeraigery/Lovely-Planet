"""Tests for the Flask application endpoints."""

import json

import pytest

from lovelyplanet.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data["status"] == "ok"


def test_greet(client):
    response = client.get("/greet/world")
    assert response.status_code == 200
    assert b"world" in response.data


def test_parse_yaml(client):
    response = client.post(
        "/parse-yaml",
        data="name: test\nvalue: 42",
        content_type="text/plain",
    )
    data = json.loads(response.data)
    assert data["name"] == "test"
    assert data["value"] == 42


def test_fetch_missing_url(client):
    response = client.get("/fetch")
    assert response.status_code == 400


def test_encrypt(client):
    response = client.post(
        "/encrypt",
        data="hello world",
        content_type="text/plain",
    )
    data = json.loads(response.data)
    assert "encrypted" in data
