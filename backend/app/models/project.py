"""
Project database model.
"""

from typing import Optional
from typing import TYPE_CHECKING

from sqlmodel import Field
from sqlmodel import SQLModel
from sqlmodel import Relationship
if TYPE_CHECKING:
    from app.models.feature import Feature

from app.models.project_technology import (
    ProjectTechnology,
)

class Project(SQLModel, table=True):
    """
    Portfolio project entity.
    """

    __tablename__ = "projects"

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
    )

    name: str

    description: str

    status: str

    featured: bool = False

    github_url: str | None = None

    demo_url: str | None = None

    features: list["Feature"] = Relationship(
    back_populates="project"
    )

    technologies: list[
        "ProjectTechnology"
    ] = Relationship(
        back_populates="project"
    )