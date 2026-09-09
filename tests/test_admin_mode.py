import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_signup_requires_teacher_login():
    response = client.post(
        "/activities/Chess%20Club/signup?email=student@example.com"
    )

    assert response.status_code == 403
    assert "Teacher login required" in response.json()["detail"]


def test_unregister_requires_teacher_login():
    response = client.delete(
        "/activities/Chess%20Club/unregister?email=michael@mergington.edu"
    )

    assert response.status_code == 403
    assert "Teacher login required" in response.json()["detail"]
