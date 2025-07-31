
import requests


from src.configuration import SERVICE_URL


from src.schemas.post2 import POST_SCHEMA
from src.baseclasses.response import Response

from src.enum.global_enums import GlobalErrorMessages

def test_get_one_booking_schema():
    response = requests.get(url=SERVICE_URL)
    response = Response(response)
    response.assert_status_code(200).validate(POST_SCHEMA)



