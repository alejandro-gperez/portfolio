"""
Project feature database model.
"""

from typing import Optional

from sqlmodel import Field
from sqlmodel import SQLModel


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