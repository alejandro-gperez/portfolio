"""
Project feature database model.
"""

from typing import Optional
from typing import TYPE_CHECKING

from sqlmodel import Field
from sqlmodel import SQLModel
from sqlmodel import Relationship
if TYPE_CHECKING:
    from app.models.project import Project


class Feature(SQLModel, table=True):
    """
    Project feature entity.
    """

    __tablename__ = "features"

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
    )

    project_id: int = Field(
        foreign_key="projects.id"
    )

    name: str

    project: "Project" = Relationship(
    back_populates="features"
    )