from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .repositories import (
    CmsSystemRepository,
    ProjectRepository,
    ProjectExtensionRepository,
)
from .schemas import (
    CmsSystemResponse,
    CmsSystemCreate,
    ProjectResponse,
    ProjectCreate,
    ProjectExtensionResponse,
    ProjectExtensionCreate,
)


class CmsSystemService:
    def __init__(self, db: Session):
        self.repository = CmsSystemRepository(db)

    def get_all(self) -> list[CmsSystemResponse]:
        users = self.repository.get_all()
        return [CmsSystemResponse.model_validate(user) for user in users]

    def get_by_id(self, id: int) -> CmsSystemResponse:
        user = self.repository.get_by_id(id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"CMS с id {id} не найден",
            )

        return CmsSystemResponse.model_validate(user)

    def create(self, data: CmsSystemCreate) -> CmsSystemResponse:
        user = self.repository.create(data)
        return CmsSystemResponse.model_validate(user)


class ProjectService:
    def __init__(self, db: Session):
        self.repository = ProjectRepository(db)

    def get_all(self) -> list[ProjectResponse]:
        users = self.repository.get_all()
        return [ProjectResponse.model_validate(user) for user in users]

    def get_by_id(self, id: int) -> ProjectResponse:
        user = self.repository.get_by_id(id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Проект с id {id} не найден",
            )

        return ProjectResponse.model_validate(user)

    def create(self, data: ProjectCreate) -> ProjectResponse:
        user = self.repository.create(data)
        return ProjectResponse.model_validate(user)


class ProjectExtensionService:
    def __init__(self, db: Session):
        self.repository = ProjectExtensionRepository(db)

    def get_by_id(self, id: int) -> ProjectExtensionResponse:
        user = self.repository.get_by_id(id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Расширенные поля с id {id} не найдены",
            )

        return ProjectExtensionResponse.model_validate(user)

    def create(self, data: ProjectExtensionCreate) -> ProjectExtensionResponse:
        user = self.repository.create(data)
        return ProjectExtensionResponse.model_validate(user)
