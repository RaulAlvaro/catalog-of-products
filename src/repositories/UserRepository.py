from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session

from src.configs.database import get_db_connection
from src.models.UserModel import User

class UserRepository:
    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def get_user(self, user: User) -> User:
        return self.db.get(
            User,
            user.id,
        )
    
    def get_all_users(
        self,
    ) -> List[User]:
        query = self.db.query(User)
        return query.all()
    
    def create_user(
        self,
        user: User
    ):
        db_user = User(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user