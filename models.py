# this model is using pydantic - for data validation and settings

from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

# User class will extend BaseModel
# Inside class can add attributes
# optional and data type is UUID, if not provided use uuid4
# gender will be an Enum, which is choices we specify? import Enum and pass in class name to the attribute
# if doesn't have Optional, is not nullable
# id is automatically the pk
# roles will be a list of strings, from the options in Role


class Gender(str, Enum):
    male = "male"
    female = "female"


class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]
