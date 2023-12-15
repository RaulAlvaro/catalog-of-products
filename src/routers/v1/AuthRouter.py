from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from typing_extensions import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


from src.schemas.TokenSchema import Token

from src.services.TokenService import TokenService

AuthRouter = APIRouter(tags=["auth"])

@AuthRouter.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    tokenService: TokenService = Depends(),
):
  return tokenService.get_token(form_data)