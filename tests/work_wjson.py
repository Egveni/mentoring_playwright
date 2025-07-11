
import requests

from jsonschema import validate

from src.configuration import SERVICE_URL

from src.enum.global_enums import GlobalErrorMessages

def test_getting_post():
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    json_data = response.json()
    print(json_data)
    #validate(instance=json_data, schema={


