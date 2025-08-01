from enum import Enum


from pydantic import field_validator

class Statuses(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    
    @classmethod
    def _missing_(cls, value):
        # Поддержка case-insensitive значений
        if isinstance(value, str):
            for member in cls:
                if member.value.lower() == value.lower():
                    return member
        return None

class Genders(Enum):
    FEMALE = "female"  
    MALE = "male"      

# class Statuses(Enum):
#     ACTIVE = "ACTIVE"
#     INACTIVE = "INACTIVE"

class UserErrors(Enum):
    WRONG_EMAIL = "Email must contain @"  