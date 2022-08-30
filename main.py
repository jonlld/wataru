# type import
from http.client import HTTPException
from typing import List
from uuid import UUID, uuid4
# FastAPI
from fastapi import FastAPI, HTTPException
# from our models.py
from models import User, Gender, Role

app = FastAPI()

# what syntax is this? also, not highlighted...
db: List[User] = [
    User(
        # id=uuid4(),
        id=UUID("c7a09d0b-ac43-4ab5-ab1a-55c626fe0953"),
        first_name="Jamila",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("c0975c1e-82fa-4343-b0a0-654f077f23cb"),
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


# submit a new user - same endpoint, different method
# will receive a user of type User

@app.post("/api/v1/users")
async def register_user(user: User):
    # takes user from req body and appends
    db.append(user)
    # send id back to client
    return {"id": user.id}


# delete user endpoint
# using a 'path variable'


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )
