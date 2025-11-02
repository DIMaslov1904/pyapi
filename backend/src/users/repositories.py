from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self) -> list[User]:
        return self.db.query(User).all()
    
    def get_by_id(self, id:int) -> User | None:
        return self.db.query(User).filter(User.id == id).first()