from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel

# Class will extend BaseModel
# Add attributes
class UserRequest(BaseModel):
    request_string: str
    request_lang: str


# make a new class, all optional for update
# as put requests will be in this format


class Phrase(BaseModel):
    text: str
    translation: str
