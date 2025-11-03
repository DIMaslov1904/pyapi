from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str = Field(..., min_length=2, max_length=50, description="Логин")


class UserAuth(UserBase):
    password: str = Field(..., description="Пароль")


class UserCreate(UserBase):
    email: str = Field(..., min_length=6, max_length=120, description="E-mail")
    name: str = Field(..., min_length=2, max_length=50, description="Имя")
    last_name: str = Field(..., min_length=2, max_length=50, description="Фамилия")


class UserResponse(UserCreate):
    id: int = Field(..., description="id")

    class Config:
        from_attributes = True


class UserListResponse(BaseModel):
    users: list[UserResponse] = Field(..., description="Список сотрудников")
    total: int = Field(..., description="Количество сотрудников")
