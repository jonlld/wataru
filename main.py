# type import
from typing import List
from uuid import uuid4
# FastAPI
from fastapi import FastAPI
# from our models.py
from models import User, Gender, Role

app = FastAPI()

# what syntax is this? also, not highlighted...
db: List[User] = [
    User(
        id=uuid4(),
        first_name="Jamila",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Alex",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]


@app.get("/")
def root():
    return {"Hello": "Everyone!"}


# simple endpoint to serve users list
@app.get("/api/v1/users")
async def fetch_users():
    return db
