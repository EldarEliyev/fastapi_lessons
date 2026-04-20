from fastapi.testclient import TestClient
from intro_43_pytest import app 

client = TestClient(app)

def test_read_welcome():
    response =  client.get("/welcome")
    assert response.status_code == 200
    assert response.json() == {"message":  "Welcome Eldar!"}


def test_calculate_sum():
    response = client.get("/sum",  params={"a": 10,  "b": 20})
    assert response.status_code == 200 
    assert response.json()["result"] == 30