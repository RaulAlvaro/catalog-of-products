from typing import List

from fastapi import APIRouter, Depends

from src.schemas.UserSchema import UserBaseSchema, UserCreateSchema, UserSchema

from src.services.UserService import UserService

UserRouter = APIRouter(tags=["user"])

@UserRouter.get("/users/", response_model=List[UserBaseSchema])
def get_users(userService: UserService = Depends()):
    return userService.get_all_users()

@UserRouter.get("/users/{user_id}", response_model=UserSchema)
def get_user(user_id: int, userService: UserService = Depends()):
    return userService.get_user(user_id)

@UserRouter.post("/users/", response_model=UserSchema)
def create_user(user: UserCreateSchema, userService: UserService = Depends()):
    return userService.create_user(user)