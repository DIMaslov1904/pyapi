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
    ProjectListResponse,
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
        self.project_repository = ProjectRepository(db)
        self.project_extension_repository = ProjectExtensionRepository(db)

    def get_all(self) -> ProjectListResponse:
        projects = self.project_repository.get_all()
        projects_response = [ProjectResponse.model_validate(item) for item in projects]
        return ProjectListResponse(projects=projects_response, total=len(projects_response))

    def get_by_id(self, id: int) -> ProjectResponse:
        project = self.project_repository.get_by_id(id)
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Проект с id {id} не найден",
            )

        return ProjectResponse.model_validate(project)

    def create(self, data: ProjectCreate) -> ProjectResponse:
        user = self.repository.create(data)
        return ProjectResponse.model_validate(user)


