
import requests
from src.configuration import SERVICE_URL
from src.test_tools import get_first_booking_id, get_auth_token

from src.enum.global_enums import GlobalErrorMessages


def test_delete_request(auth_token):
    
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={auth_token}"
    }
    
    first_booking_id = get_first_booking_id(SERVICE_URL)
    response = requests.delete(SERVICE_URL + f"{first_booking_id}", headers=headers)

    assert response.status_code == 201 or response.status_code == 200, \
        f"Expected 200/201, got {response.status_code}"

    print(f"Booking {first_booking_id} deleted. Status code: {response.status_code}")


def test_patch_existing_booking(auth_token):

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={auth_token}"
    }

    patch_data = {
        "firstname": "Alice",
        "lastname": "Smith"
    }

    first_booking_id = get_first_booking_id(SERVICE_URL)
    response = requests.patch(
        url=SERVICE_URL + f"{first_booking_id}", 
        json=patch_data, 
        headers=headers
    )

    assert response.status_code == 200, \
        f"PATCH failed: {response.status_code}, Response: {response.text}"

    updated = response.json()
    assert updated["firstname"] == patch_data["firstname"]
    assert updated["lastname"] == patch_data["lastname"]

    print(f"Booking {first_booking_id} успешно обновлён.")
    print("Обновлённые данные:", updated)