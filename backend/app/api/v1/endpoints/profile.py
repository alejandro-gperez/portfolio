"""
Profile API endpoints.

Provides public profile information displayed throughout
the portfolio application.
"""

from fastapi import APIRouter

from app.schemas.profile import ProfileResponse

router = APIRouter()


@router.get("/", response_model=ProfileResponse)
def get_profile() -> ProfileResponse:
    """
    Retrieve public profile information.

    Returns:
        ProfileResponse: Developer profile data.
    """
    return ProfileResponse(
        name="Alejandro Perez",
        title="Backend Engineer",
        bio="Building APIs, data pipelines and scalable systems.",
        github_url="https://github.com/your-username",
        linkedin_url="https://linkedin.com/in/your-profile",
        email="your-email@example.com",
        location="Guatemala",
        profile_image_url="https://example.com/profile.jpg",
    )