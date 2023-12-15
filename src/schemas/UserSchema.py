from pydantic import BaseModel

class UserBaseSchema(BaseModel):
    username: str
    email: str
    

class UserCreateSchema(UserBaseSchema):
    hashed_password: str

class UserSchema(UserBaseSchema):
    id: int
    hashed_password: str
    is_active: bool
    
    class Config:
        from_attributes = True