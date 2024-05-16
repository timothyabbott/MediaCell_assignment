from fastapi.testclient import TestClient

from fastAPI_main import app

client = TestClient(app)


# This will not be a list
def test_id_from_codeword():
    response = client.get("/actions/id/5002")
    assert response.status_code == 200
    assert response.json() == 'thanks'


def test_code_from_action():
    response = client.get("/actions/codeword/alert")
    assert response.status_code == 200
    assert response.json() == [5000,5001]
