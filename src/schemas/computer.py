from pydantic import BaseModel, HttpUrl, UUID4, EmailStr
from pydantic.types import PastDate, FutureDate
from typing import List
from pydantic.networks import IPv4Address, IPv6Address
from pydantic_extra_types.color import Color


from pydantic_extra_types.payment import PaymentCardNumber

from examples import computer

from src.enum.user_enums import Statuses, UserErrors

class PhysicalInfo(BaseModel):
    color: Color
    photo: HttpUrl
    uuid: UUID4

class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr


class DetailedInfo(BaseModel):
    physical: PhysicalInfo
    owners: List[Owners]


class Computer(BaseModel):
    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo


comp = Computer.model_validate(computer)

print(comp)