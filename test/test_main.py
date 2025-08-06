from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_send_email_success(monkeypatch):
    # Monkeypatch the Mailgun request to avoid sending real emails
    def mock_post(url, auth, data):
        class MockResponse:
            status_code = 200
            def json(self):
                return {"message": "Queued. Thank you."}
        return MockResponse()

    import requests
    monkeypatch.setattr(requests, "post", mock_post)

    response = client.post("/send-email/", json={
        "to": "test@example.com",
        "subject": "Test Email",
        "message": "This is a test email"
    })

    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_send_email_failure(monkeypatch):
    # Simulate Mailgun failure response
    def mock_post(url, auth, data):
        class MockResponse:
            status_code = 500
            text = "Mailgun error"
        return MockResponse()

    import requests
    monkeypatch.setattr(requests, "post", mock_post)

    response = client.post("/send-email/", json={
        "to": "test@example.com",
        "subject": "Test Email",
        "message": "This should fail"
    })

    assert response.status_code == 500
    assert "Mailgun error" in response.text
