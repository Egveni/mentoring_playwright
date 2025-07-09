
import requests
from src.configuration import SERVICE_URL

from src.enum.global_enums import GlobalErrorMessages

def test_getting_post():
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 200
    json_data = response.json()
    print(json_data)


def test_authentication():
    
    auth_url = "https://restful-booker.herokuapp.com/auth"
    data = {
        "username": "admin",
        "password": "password123"
    }

    auth_response = requests.post(auth_url, json=data)

    token = auth_response.json().get("token")
    print(f"Token: {token}")


def test_getting2_post():
    response = requests.get(url=SERVICE_URL + "895")
    assert response.status_code == 200
    json_data = response.json()
    print(json_data)


def test_post_request():
    
    payload = {
        "firstname": "Jim",
        "lastname": "Brown", 
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    
    response = requests.post(
        url=SERVICE_URL,
        json=payload,
        headers={'Content-Type': 'application/json'}
    )
    
    assert response.status_code == 200
    
    data = response.json()
    

    booking = data['booking']
    assert booking['firstname'] == payload['firstname']
    assert booking['lastname'] == payload['lastname']
    assert booking['totalprice'] == payload['totalprice']
    assert booking['depositpaid'] == payload['depositpaid']
    assert booking['bookingdates']['checkin'] == payload['bookingdates']['checkin']
    assert booking['bookingdates']['checkout'] == payload['bookingdates']['checkout']
    assert booking['additionalneeds'] == payload['additionalneeds']
    
    print(f"Created booking with ID: {data['bookingid']}")
    print(f"Response data: {data}")

def test_put_request():
    auth_url = "https://restful-booker.herokuapp.com/auth"
    data = {
        "username": "admin",
        "password": "password123"
    }
    auth_response = requests.post(auth_url, json=data)
    token = auth_response.json().get("token")
    if not token:
        raise Exception(GlobalErrorMessages.WRONG_STATUS_CODE.value)
    print(f"Token: {token}")

    payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={token}'
    }

    response = requests.put(
        url=SERVICE_URL + "895",
        json=payload,
        headers=headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data['firstname'] == payload['firstname']
    assert data['lastname'] == payload['lastname']
    assert data['totalprice'] == payload['totalprice']
    assert data['depositpaid'] == payload['depositpaid']
    assert data['bookingdates']['checkin'] == payload['bookingdates']['checkin']
    assert data['bookingdates']['checkout'] == payload['bookingdates']['checkout']
    assert data['additionalneeds'] == payload['additionalneeds']

    print(f"Updated booking with ID: 895")
    print(f"Response data: {data}")


def test_delete_request():

    auth_url = "https://restful-booker.herokuapp.com/auth"
    data = {
        "username": "admin",
        "password": "password123"
    }
    auth_response = requests.post(auth_url, json=data)
    token = auth_response.json().get("token")
    if not token:
        raise Exception(GlobalErrorMessages.WRONG_STATUS_CODE.value)
    print(f"Token: {token}")


    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }

    response = requests.delete(SERVICE_URL + "3", headers=headers)

    assert response.status_code == 201 or response.status_code == 200, \
        f"Expected 200/201, got {response.status_code}"

    print(f"Booking 720 deleted. Status code: {response.status_code}")

def test_healthcheck_get():
    
    response = requests.get(url="https://restful-booker.herokuapp.com/ping")
    
    assert response.status_code == 201 or response.status_code == 200, \
        f"Expected 200/201, got {response.status_code}"
    
    try:
        json_data = response.json()
        print("Response JSON:", json_data)
    except ValueError:
        print("No JSON in response (which is OK for /ping)")
        print("Raw response text:", response.text)


def test_patch_existing_booking():

    auth_url = "https://restful-booker.herokuapp.com/auth"
    credentials = {
        "username": "admin",
        "password": "password123"
    }
    auth_response = requests.post(auth_url, json=credentials)
    token = auth_response.json().get("token")
    assert token, "Token not received"
    print(f"Token: {token}")

    patch_data = {
        "firstname": "Alice",
        "lastname": "Smith"
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}"
    }

    booking_id = "231"
    response = requests.patch(url=SERVICE_URL + booking_id, json=patch_data, headers=headers)

    assert response.status_code == 200, f"PATCH failed: {response.status_code}, Response: {response.text}"

    updated = response.json()
    assert updated["firstname"] == patch_data["firstname"]
    assert updated["lastname"] == patch_data["lastname"]

    print(f"Booking {booking_id} успешно обновлён.")
    print("Обновлённые данные:", updated)