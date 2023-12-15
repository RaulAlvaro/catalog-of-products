from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Union
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status

from src.repositories.UserRepository import UserRepository
from src.schemas.UserSchema import UserCreateSchema


import os
from dotenv import load_dotenv

# ----
# Auth
# ----
BASE_DIR= os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = os.environ['SECRET_KEY']
ALGORITHM = os.environ['ALGORITHM']
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ['ACCESS_TOKEN_EXPIRE_MINUTES']
ACCESS_TOKEN_EXPIRE_MINUTES = int(ACCESS_TOKEN_EXPIRE_MINUTES)
# ----

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class TokenService:
    userRepository: UserRepository

    def __init__(
            self, userRepository: UserRepository = Depends()
    ) -> None:
        self.userRepository = userRepository

    # @staticmethod
    def verify_password(self, plain_password, hashed_password):
      return pwd_context.verify(plain_password, hashed_password)

    # @staticmethod
    def get_password_hash(self, password):
        return pwd_context.hash(password)


    def get_user(self, users_list, username: str):
        user = [user for user in users_list if user.username == username]
        [user] = user
        print("user", user)
        if user:
            return user

    def authenticate_user(self, list_users, username: str, password: str):
        user = self.get_user(list_users, username)
        if not user:
            return False
        if not self.verify_password(password, user.hashed_password):
            return False
        return user


    def create_access_token(self, data: dict, expires_delta: Union[timedelta, None] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    def get_token(self, form_data):
        users_in_db = self.userRepository.get_all_users()
        users_list = [UserCreateSchema(**user.__dict__) for user in users_in_db]
        user = self.authenticate_user(users_list, form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}        