from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Access(Base):
    __tablename__ = 'accesses'
    id = Column(Integer, primary_key=True)
    login = Column(String(50), unique=True, nullable=False)
    password = Column(String(120), nullable=False)


    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    user = relationship('User', backref='accesses')

    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False, index=True)
    project = relationship('Project', backref='accesses')

    def __repr__(self):
        return f'<Access to project {self.project_id} by user {self.user_id} [{self.id}]>'