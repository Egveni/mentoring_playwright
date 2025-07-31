
import requests


def get_first_booking_id(SERVICE_URL):
        response = requests.get(url=SERVICE_URL)
        json_data = response.json()
        print(json_data[0])
        if json_data is None:
            raise ValueError("Response JSON is None")
        else:
            return json_data[0]['bookingid']

def get_auth_token(username="admin", password="password123"):
    auth_url = "https://restful-booker.herokuapp.com/auth"
    data = {
        "username": username,
        "password": password
    }
    
    auth_response = requests.post(auth_url, json=data)
    
    token = auth_response.json().get("token")
    
    if not token:
        raise Exception("Токен не получен")
    else:
        print(f"Токен получен: {token}")    
        return token
    
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

