from fastapi import Depends, FastAPI

# from configs.enviroment import get_environment_variables
from src.routers.v1.UserRouter import UserRouter
from src.routers.v1.ProductRouter import ProductRouter
from src.routers.v1.ReportRouter import ReportRouter
from src.routers.v1.AuthRouter import AuthRouter

from src.models.BaseModel import init

# Application Environment Configuration
# env = get_environment_variables()

app = FastAPI()

app.include_router(UserRouter)
app.include_router(ProductRouter)
app.include_router(ReportRouter)
app.include_router(AuthRouter)

# Initialise Data Model Attributes
init()