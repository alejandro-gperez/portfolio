"""
Projects API endpoints.

Provides project information showcased in the portfolio.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_projects() -> list[dict]:
    """
    Retrieve featured portfolio projects.

    Returns:
        list[dict]: Project summaries.
    """
    return [
        {
            "id": 1,
            "name": "Portfolio SaaS",
            "status": "In Progress",
            "featured": True,
            "stack": [
                "FastAPI",
                "PostgreSQL",
                "React",
            ],
        }
    ]