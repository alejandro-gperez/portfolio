"""
Profile API endpoints.

Provides public profile information displayed throughout
the portfolio application.
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlmodel import Session

from app.core.database import get_session
from app.schemas.profile import ProfileResponse
from app.services.profile_service import ProfileService

router = APIRouter()


@router.get("/", response_model=ProfileResponse)
def get_profile(
    session: Session = Depends(get_session),
) -> ProfileResponse:
    """
    Retrieve profile information.
    """

    profile = ProfileService.get_profile(session)

    if profile is None:
        raise HTTPException(
            status_code=404,
            detail="Profile not found",
        )

    return ProfileResponse(
        name=profile.name,
        title=profile.title,
        bio=profile.bio,
        github_url=profile.github_url,
        linkedin_url=profile.linkedin_url,
        email=profile.email,
        location=profile.location,
        profile_image_url=profile.profile_image_url,
    )