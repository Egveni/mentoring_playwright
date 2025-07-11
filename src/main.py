import requests
class A:
    x = 1
    def some_method(self):
        return "This is a method in class A"


url = "https://restful-booker.herokuapp.com/booking/221803"
responce = requests.get(url)
print(responce.json())