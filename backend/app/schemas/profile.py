"""
Profile response schemas.
"""

from pydantic import BaseModel, HttpUrl


class ProfileResponse(BaseModel):
    """
    Public developer profile information.
    """

    name: str
    title: str
    bio: str
    github_url: HttpUrl
    linkedin_url: HttpUrl
    email: str
    location: str
    profile_image_url: HttpUrl