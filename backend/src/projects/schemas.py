from datetime import datetime
from pydantic import BaseModel, Field
from src.users.schemas import UserResponse


class CmsSystemBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Название CMS")
    base_admin_url: str | None = Field(
        None,
        min_length=2,
        max_length=120,
        description="Стандартный путь до админ панели",
    )


class CmsSystemCreate(CmsSystemBase):
    pass


class CmsSystemResponse(CmsSystemBase):
    id: int = Field(..., description="id")

    class Config:
        form_attributes = True


class CmsSystemListResponse(BaseModel):
    cms_systems: list[CmsSystemResponse] = Field(..., description="CMS системы")
    total: int = Field(..., description="Количество CMS систем")


class ProjectExtensionBase(BaseModel):
    user_id: int = Field(..., description="id ответственного за проект сотрудника")
    git: str | None = Field(
        None, min_length=11, max_length=120, description="URL адрес к Git-репозиторию"
    )
    figma: str | None = Field(
        None, min_length=11, max_length=120, description="URL адрес к Figma"
    )
    cms_system_id: int | None = Field(None, description="id CMS системы")
    custom_admin_url: str | None = Field(
        None,
        min_length=2,
        max_length=120,
        description="Не стандартный URL адрес до админ панели",
    )
    auto_deploy: bool = Field(..., description="Настроен ли авто-деплой")
    project_id: int = Field(..., description="id проекта")


class ProjectExtensionCreate(ProjectExtensionBase):
    pass


class ProjectExtensionResponse(BaseModel):
    id: int = Field(..., description="id")
    user: UserResponse = Field(..., description="Ответственный за проект сотрудник")


class ProjectBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Название проекта")
    url: str = Field(
        ..., min_length=11, max_length=120, description="URL адрес проекта"
    )
    description: str | None = Field(
        None, max_length=5000, description="Описание проекта"
    )
    document: str = Field(
        ..., min_length=11, max_length=120, description="URL адрес к документации"
    )


class ProjectCreate(ProjectBase):
    pass


class ProjectResponse(ProjectBase):
    id: int = Field(..., description="id")
    created_at: datetime = Field(..., description="Время добавления проекта")
    extensions: ProjectExtensionResponse = Field(
        ..., description="Расширенная информация по проекту"
    )

    class Config:
        form_attributes = True


class ProjectListResponse(BaseModel):
    projects: list[ProjectResponse] = Field(..., description="Список проектов")
    total: int = Field(..., description="Количество проектов")
