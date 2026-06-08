"""
Project-Technology relationship model.
"""

from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.project import Project
    from app.models.technology import (
        Technology,
    )


class ProjectTechnology(
    SQLModel,
    table=True,
):
    """
    Many-to-many relationship between
    projects and technologies.
    """

    __tablename__ = (
        "project_technologies"
    )

    project_id: int = Field(
        foreign_key="projects.id",
        primary_key=True,
    )

    technology_id: int = Field(
        foreign_key="technologies.id",
        primary_key=True,
    )

    project: "Project" = Relationship(
        back_populates="technologies"
    )

    technology: "Technology" = (
        Relationship(
            back_populates="projects"
        )
    )