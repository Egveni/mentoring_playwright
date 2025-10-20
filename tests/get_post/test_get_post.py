
import requests
from src.configuration import SERVICE_URL, PING_URL
from tools_for_tests import get_first_booking_id

from src.enum.global_enums import GlobalErrorMessages
from src.schemas.get_validate import Booking, BookingDates, Booking_one, CreatedBookingResponse
from pydantic import TypeAdapter, ValidationError
from typing import List



def test_get_all_bookings():
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    json_data = response.json()
    print(json_data)



# выводим все и сразу валидация что в массиве 
def test_get_all_bookings_with_validation():
    # Получаем данные из API
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    
    json_data = response.json()
    
    try:
        bookings_validator = TypeAdapter(List[Booking])
        validated_bookings = bookings_validator.validate_python(json_data)
        
        # Выводим информацию о валидированных данных
        print(f"Successfully validated {len(validated_bookings)} bookings")
    except ValidationError as error:
            print(f" Validation failed: {error}")
            raise AssertionError(f"Booking validation failed: {error}")


#выводим один и сразу валидация его полей
def test_get_one_booking():
    first_booking_id = get_first_booking_id(SERVICE_URL)
    response = requests.get(url=SERVICE_URL+f"{first_booking_id}")
    assert response.status_code == 200
    try:

        json_data = response.json()
        # Создаем валидатор для списка букингов
        TypeAdapter(Booking_one).validate_python(json_data)
        
        print(f"Successfully validated booking with ID: {first_booking_id}")
    
    except ValidationError as e:
        print(f"Validation failed: {e}")
        raise AssertionError(f"Booking validation failed: {e}")



#постим и сразу проверяем, что запостился с корректной структурой
def test_post_booking():
    
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
    
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value

    json_data = response.json()
    validated_response = CreatedBookingResponse(**json_data)

    print(f"Created booking with ID: {validated_response.bookingid}")
    print(f"Booking data: {validated_response.booking}")



def test_healthcheck_get():
    
    response = requests.get(url=PING_URL)
    
    assert response.status_code == 201 or response.status_code == 200, \
        f"Expected 200/201, got {response.status_code}"
    
    try:
        json_data = response.json()
        print("Response JSON:", json_data)
    except ValueError:
        print("No JSON in response (which is OK for /ping)")
        print("Raw response text:", response.text)