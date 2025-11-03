from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.database import get_db
from .models import User
from .services import UserService

router = APIRouter(
    prefix="/api/users",
    tags=["👥 Пользователи"],
)

# response_model=list[User],

@router.get("/", status_code=status.HTTP_200_OK, summary="Получить список пользователей")
async def get_all(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_all()

# response_model=User, 
@router.get("/{user_id}", status_code=status.HTTP_200_OK, summary="Получить пользователя по id")
async def get_by_id(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_by_id(user_id)
