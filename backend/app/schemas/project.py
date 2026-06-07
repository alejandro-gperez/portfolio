"""
Project response schemas.
"""

from pydantic import BaseModel, HttpUrl


class FeatureResponse(BaseModel):
    """
    Project feature representation.
    """

    name: str


class ProjectResponse(BaseModel):
    """
    Portfolio project representation.
    """

    id: int
    name: str
    description: str
    status: str
    featured: bool

    github_url: HttpUrl | None = None
    demo_url: HttpUrl | None = None

    stack: list[str]
    features: list[FeatureResponse]