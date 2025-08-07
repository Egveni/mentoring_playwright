import pytest
import requests

@pytest.fixture(scope="session")
def auth_token():
    """Получает токен авторизации для всей сессии тестов"""
    auth_url = "https://restful-booker.herokuapp.com/auth"
    data = {
        "username": "admin",
        "password": "password123"
    }
    
    auth_response = requests.post(auth_url, json=data)
    
    assert auth_response.status_code == 200, f"Auth failed: {auth_response.status_code}"
    
    token = auth_response.json().get("token")
    
    if not token:
        raise Exception("Токен не получен")
    
    print(f"Токен получен: {token}")
    return token