from fastapi.testclient import TestClient

from fastAPI_main import app

client = TestClient(app)


def test_action_from_code():
    response = client.get("/actions/codeword/5002")
    assert response.status_code == 200
    assert response.json() == 'thanks'


def test_code_from_action():
    response = client.get("/actions/code/thanks")
    assert response.status_code == 200
    assert response.json() == 5002
