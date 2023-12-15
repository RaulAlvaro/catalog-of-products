from typing import List
from fastapi import Depends
from src.models.UserModel import User
from src.repositories.UserRepository import UserRepository
from src.schemas.UserSchema import UserCreateSchema

class UserService:
    userRepository: UserRepository

    def __init__(
        self, userRepository: UserRepository = Depends()
    ) -> None:
        self.userRepository = userRepository

    def get_user(self, user_id: int) -> User:
        return self.userRepository.get_user(
            User(id=user_id)
        )
    
    def get_all_users(
        self
    ) -> List[User]:
        return self.userRepository.get_all_users()
    
    def create_user(
        self,
        user: UserCreateSchema
    ) -> User:
        return self.userRepository.create_user(user)