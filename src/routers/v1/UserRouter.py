from typing import List

from fastapi import APIRouter, Depends, HTTPException

from src.schemas.UserSchema import UserBaseSchema, UserCreateSchema, UserSchema
from typing_extensions import Annotated


from src.services.UserService import UserService

from src.utils.auth import get_current_active_user

UserRouter = APIRouter(tags=["user"])

@UserRouter.get("/users/", response_model=List[UserBaseSchema])
def get_users(current_user: Annotated[UserBaseSchema, Depends(get_current_active_user)], userService: UserService = Depends()):
    if current_user:
        return userService.get_all_users()
    raise HTTPException(status_code=400, detail="User not found")

@UserRouter.get("/users/{user_id}", response_model=UserSchema,)
def get_user(current_user: Annotated[UserBaseSchema, Depends(get_current_active_user)], user_id: int, userService: UserService = Depends()):
    if current_user:
        return userService.get_user(user_id)
    raise HTTPException(status_code=400, detail="User not found")

@UserRouter.get("/user/me/", response_model=UserSchema)
def get_user_detail(current_user: Annotated[UserBaseSchema, Depends(get_current_active_user)]):
    if current_user:
        return current_user
    raise HTTPException(status_code=400, detail="User not found")

@UserRouter.post("/users/", response_model=UserSchema)
def create_user(user: UserCreateSchema, userService: UserService = Depends()):
    return userService.create_user(user)
