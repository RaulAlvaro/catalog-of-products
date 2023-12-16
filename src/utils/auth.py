from jose import JWTError, jwt
from typing_extensions import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.schemas.UserSchema import UserSchema
from src.schemas.TokenSchema import Token, TokenData
from src.services.UserService import UserService

import os
from dotenv import load_dotenv


SECRET_KEY = os.environ['SECRET_KEY']
ALGORITHM = os.environ['ALGORITHM']
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ['ACCESS_TOKEN_EXPIRE_MINUTES']
ACCESS_TOKEN_EXPIRE_MINUTES = int(ACCESS_TOKEN_EXPIRE_MINUTES)
# ----

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], userService: UserService = Depends()):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    users_in_db = userService.get_all_users()
    users_list = [UserSchema(**user.__dict__) for user in users_in_db]
    user = get_user(users_list, username=token_data.username)
    print("user in get_current_user", user)
    if user is None:
        raise credentials_exception
    return user


def get_current_active_user(
    current_user: Annotated[UserSchema, Depends(get_current_user)],
):
    if not(current_user.is_active):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def get_user(users_list, username: str):
    user = [user for user in users_list if user.username == username]
    [user] = user
    print("user", user)
    if user:
        return user