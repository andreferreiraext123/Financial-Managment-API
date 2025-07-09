from fastapi import APIRouter, HTTPException
from models.security import UserIn
from storage.memory import users

from security.security import get_password_hash

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
async def get_all_users():
    return {
        "Users": users
    }

@router.post("/", status_code=201)
async def add_user(user: UserIn):
    #user.password = get_password_hash(user.password)
    users.append(user)
    return {"received": user}
