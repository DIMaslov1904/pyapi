from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from src.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True)
    password = Column(String(120), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.username} [{self.id}]>'
