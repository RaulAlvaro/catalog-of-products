from fastapi import Depends, FastAPI

# from configs.enviroment import get_environment_variables
from src.routers.v1.UserRouter import UserRouter
from src.models.BaseModel import init

# Application Environment Configuration
# env = get_environment_variables()

app = FastAPI()

app.include_router(UserRouter)

# Initialise Data Model Attributes
init()