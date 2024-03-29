from random import random
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}


def test_get_sum():
    response = client.get("/sum", params={'a':2, 'b':4})
    assert response.status_code == 200
    assert response.json() == 6
    
    
def test_get_division_ok():
    dividend = float(random())
    divisor = float(random())
    response = client.get("/division", params={'dividend':dividend, 'divisor':divisor})
    assert response.status_code == 200
    assert response.json() == dividend/divisor
    
    
def test_get_division_by_zero():
    dividend = float(random())
    response = client.get("/division", params={'dividend':dividend, 'divisor':0})
    assert response.status_code == 400
    assert response.json() == {'detail':'Cannot divide by zero'}  