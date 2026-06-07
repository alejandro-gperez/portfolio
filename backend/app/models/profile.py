"""
Profile database model.

Represents the portfolio owner's public profile.
"""

from typing import Optional

from sqlmodel import Field
from sqlmodel import SQLModel


class Profile(SQLModel, table=True):
    """
    Portfolio profile entity.
    """

    __tablename__ = "profiles"

    id: Optional[int] = Field(
        default=None,
        primary_key=True,
    )

    name: str

    title: str

    bio: str

    github_url: str

    linkedin_url: str

    email: str

    location: str

    profile_image_url: str