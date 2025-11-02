from sqlalchemy.orm import Session, joinedload
from .models import CmsSystem, Project, ProjectExtension
from .schemas import CmsSystemCreate, ProjectCreate, ProjectExtensionCreate


class CmsSystemRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[CmsSystem]:
        return self.db.query(CmsSystem).all()

    def get_by_id(self, id: int) -> CmsSystem | None:
        return self.db.query(CmsSystem).filter(CmsSystem.id == id).first()

    def create(self, data: CmsSystemCreate) -> CmsSystem:
        db_user = CmsSystem(**data.model_dump())
        self.db.add(db_user)
        self.db.commit
        self.db.refresh(db_user)
        return db_user


class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Project]:
        return self.db.query(Project).options(joinedload(Project.extensions)).all()

    def get_by_id(self, id: int) -> Project | None:
        return (
            self.db.query(Project)
            .filter(Project.id == id)
            .options(joinedload(Project.extensions))
            .first()
        )

    def create(self, data: ProjectCreate) -> Project:
        db_user = Project(**data.model_dump())
        self.db.add(db_user)
        self.db.commit
        self.db.refresh(db_user)
        return db_user


class ProjectExtensionRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[ProjectExtension]:
        return (
            self.db.query(ProjectExtension)
            .options(joinedload(ProjectExtension.cms_systems))
            .all()
        )

    def get_by_id(self, id: int) -> ProjectExtension | None:
        return (
            self.db.query(ProjectExtension)
            .filter(ProjectExtension.id == id)
            .options(joinedload(ProjectExtension.cms_systems))
            .first()
        )

    def create(self, data: ProjectExtensionCreate) -> ProjectExtension:
        db_user = ProjectExtension(**data.model_dump())
        self.db.add(db_user)
        self.db.commit
        self.db.refresh(db_user)
        return db_user
