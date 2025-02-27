import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app


client = TestClient(app)

# Summarization Test
@patch("requests.post")
def test_summarize_text(mock_post):
    mock_post.return_value.json.return_value = [{"summary_text": "FastAPI is great!"}]
    mock_post.return_value.status_code = 200

    response = client.post("/api/summarize", json={"text": "FastAPI is great for APIs!"})

    assert response.status_code == 200
    assert response.json() == {"result": "FastAPI is great!"}


# Named Entity Recognition (NER) Test
@patch("requests.post")
def test_named_entity_recognition(mock_post):
    mock_post.return_value.json.return_value = [
        {"word": "Elon Musk", "entity_group": "PERSON"},
        {"word": "Tesla", "entity_group": "ORG"}
    ]
    mock_post.return_value.status_code = 200

    response = client.post("/api/ner", json={"text": "Elon Musk is the CEO of Tesla."})

    assert response.status_code == 200
    assert "entities" in response.json()
    assert response.json()["entities"] == [
        {"word": "Elon Musk", "entity_group": "PERSON"},
        {"word": "Tesla", "entity_group": "ORG"}
    ]
