"""
Profile API endpoints.

Provides public profile information displayed throughout
the portfolio application.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_profile() -> dict:
    """
    Retrieve public profile information.

    Returns:
        dict: Portfolio owner profile details.
    """
    return {
        "name": "Alejandro Perez",
        "title": "Backend Engineer",
        "bio": "Building APIs, data pipelines and scalable systems.",
        "github_url": "https://github.com/your-username",
        "linkedin_url": "https://linkedin.com/in/your-profile",
    }