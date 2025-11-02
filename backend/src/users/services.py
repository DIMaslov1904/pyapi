from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .repositories import UserRepository
from .schemas import UserCreate, UserResponse


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def get_all_users(self) -> list[UserResponse]:
        users = self.repository.get_all()
        return [UserResponse.model_validate(user) for user in users]

    def get_user_by_id(self, id: int) -> UserResponse:
        user = self.repository.get_by_id(id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Пользователь с id {id} не найден",
            )

        return UserResponse.model_validate(user)

    def create_user(self, data: UserCreate) -> UserResponse:
        user = self.repository.create(data)
        return UserResponse.model_validate(user)
