import json

def test_health_endpoint(client):
    response = client.get("/health/")
    assert response.status_code == 200
    body = json.loads(response.content)
    assert body["status"] == "ok"
