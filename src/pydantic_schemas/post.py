from pydantic import BaseModel, field_validator
from typing import Optional

class Post(BaseModel):
    bookingid: Optional[int] = None
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: dict
    additionalneeds: str

    @field_validator('bookingid')
    @classmethod
    def bookingid_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('bookingid must be a positive integer')
        return v



# Example usage:

#{'bookingid': 998}
#{'firstname': 'Josh', 'lastname': 'Allen', 'totalprice': 111, 
#'depositpaid': True, 'bookingdates': {'checkin': '2018-01-01', 
#'checkout': '2019-01-01'}, 'additionalneeds': 'super bowls'}