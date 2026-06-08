"""
Project database model.
"""

from typing import Optional

from sqlmodel import Field
from sqlmodel import SQLModel


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