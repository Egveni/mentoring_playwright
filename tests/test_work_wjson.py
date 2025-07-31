
import requests


from src.configuration import SERVICE_URL

from src.test_tools import get_first_booking_id

from src.schemas.post import POST_SCHEMA

from src.pydantic_schemas.post import Post

from src.baseclasses.response import Response

from src.enum.global_enums import GlobalErrorMessages

def test_get_one_booking_schema():
    first_booking_id = get_first_booking_id(SERVICE_URL)
    response_object = requests.get(url=SERVICE_URL+f"{first_booking_id}")
    response = Response(response_object)
    response.assert_status_code(200).validate(Post)


