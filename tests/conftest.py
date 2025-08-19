import pytest
import requests
import os
from dotenv import load_dotenv
from tools_for_tests import create_booking, delete_booking

from src.configuration import SERVICE_URL


load_dotenv()

@pytest.fixture(scope="session")
def auth_token():
    auth_url = "https://restful-booker.herokuapp.com/auth"

    username = os.getenv("YOUR_LOGIN")
    password = os.getenv("YOUR_PASSWORD")

    data = {
        "username": f"{username}",
        "password": f"{password}"
    }
    
    auth_response = requests.post(auth_url, json=data)
    
    assert auth_response.status_code == 200, f"Auth failed: {auth_response.status_code}"
    
    token = auth_response.json().get("token")
    
    return token



@pytest.fixture
def create_delete_booking():
    booking_id = create_booking()
    print(f"Booking created with id: {booking_id}")
    yield booking_id
    delete_booking(auth_token, booking_id, SERVICE_URL)
    print(f"\nBooking deleted with id: {booking_id}")