from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel

# Class will extend BaseModel
# Add attributes
class UserRequest(BaseModel):
    lang: str
    string: str
