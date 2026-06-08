"""
Technology database model.

Represents a technology used throughout portfolio projects.
"""

from typing import Optional

from sqlmodel import Field
from sqlmodel import Relationship
from sqlmodel import SQLModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.project_technology import (
        ProjectTechnology,
    )


class Technology(SQLModel, table=True):
    """
    Technology entity.
    """

    __tablename__ = "technologies"

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
    )

    name: str

    category: str

    projects: list["ProjectTechnology"] = (
        Relationship(
            back_populates="technology"
        )
    )