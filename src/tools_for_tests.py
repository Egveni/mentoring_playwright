
import requests
from src.configuration import SERVICE_URL


def get_first_booking_id(SERVICE_URL):
        response = requests.get(url=SERVICE_URL)
        json_data = response.json()
        print(json_data[0])
        if json_data is None:
            raise ValueError("Response JSON is None")
        else:
            return json_data[0]['bookingid']


def create_booking():
    booking_data = {
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
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    response = requests.post(
        url=SERVICE_URL,
        json=booking_data,
        headers=headers
    )
    
    assert response.status_code == 200
    json_response = response.json()
    booking_id = json_response.get('bookingid')
    
    print(f"Booking created with id: {booking_id}")
    return booking_id

def delete_booking(auth_token, booking_id, SERVICE_URL):
    
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={auth_token}"
    }
    
    response = requests.delete(f"{SERVICE_URL}/{booking_id}", headers=headers)

    return response.status_code in [200, 201] 



#var = ['a',3,True]
#var4 = var[0] #'a'
#
#var = {"a": 1, "b": 2, "c": 3}
#var2 = var["a"]
#print(var2)  # Output: 1
#
#
#response2 = [{
#        "firstname": "Jim",
#        "lastname": "Brown", 
#        "totalprice": 111,
#        "depositpaid": True,
#        "bookingdates": {
#            "checkin": "2018-01-01",
#            "checkout":{
#               "date": "2019-01-01",
#                "time": "12:00"
#            },
#        },
#        "additionalneeds": "Breakfast"
#    }]
#
#json_data = response2[0]["bookingdates"]["checkout"]["time"]
#print(json_data)

