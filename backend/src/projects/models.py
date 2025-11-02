from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base


class CmsSystem(Base):
    __tablename__ = "cms_system"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    base_admin_url = Column(String(120))

    def __repr__(self):
        return f"<CMSSystem {self.name} [{self.id}]>"


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    description = Column(Text, nullable=False)
    url = Column(String(120), index=True)
    document = Column(String(120))
    extensions = relationship("ProjectExtension", backref="project", uselist=False)

    def __repr__(self):
        return f"<Project {self.name} [{self.id}]>"


class ProjectExtension(Base):
    __tablename__ = "project_extensions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    user = relationship("User", backref="projects")

    git = Column(String(120))
    figma = Column(String(120))
    cms_system_id = Column(Integer, ForeignKey("cms_system.id"), index=True)
    cms_systems = relationship("CmsSystem")
    custom_admin_url = Column(String(120))
    auto_deploy = Column(Boolean, default=False)
    project_id = Column(Integer, ForeignKey("projects.id"), index=True)

    def __repr__(self):
        return f"<ProjectExtension to project {self.project}[{self.id}]>"
