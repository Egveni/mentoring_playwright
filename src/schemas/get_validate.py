from pydantic import BaseModel

from datetime import date
from typing import List


class Booking(BaseModel): 
    bookingid: int

class BookingsResponse(BaseModel):
    bookings: List[Booking] = []


class BookingDates(BaseModel):
    checkin: date
    checkout: date

class Booking_one(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str | None = None

class CreatedBookingResponse(BaseModel):
    bookingid: int
    booking: Booking_one


# {
#     "firstname": "Sally",
#     "lastname": "Brown",
#     "totalprice": 111,
#     "depositpaid": true,
#     "bookingdates": {
#         "checkin": "2013-02-23",
#         "checkout": "2014-10-23"
#     },
#     "additionalneeds": "Breakfast"
# }