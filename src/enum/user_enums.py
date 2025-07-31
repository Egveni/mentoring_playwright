from enum import Enum

class Genders(Enum):
    FEMALE = "female"  
    MALE = "male"      

class Statuses(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class UserErrors(Enum):
    WRONG_EMAIL = "Email must contain @"  