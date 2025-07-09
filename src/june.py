import requests
 
url = "https://restful-booker.herokuapp.com/booking/"
response = requests.get(url)
print(response.json())