from pydantic import BaseModel, validator
from src.enum.user_enums import Genders, Statuses, UserErrors

class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Statuses


    @validator('email')
    def check_that_dog_sign_in_email(cls, email):
        if '@' not in email:
            raise ValueError(UserErrors.WRONG_EMAIL.value)
        return email
    