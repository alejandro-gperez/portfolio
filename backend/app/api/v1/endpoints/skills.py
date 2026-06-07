"""
Skills API endpoints.

Provides categorized technical skills used in the
Engineering Overview section of the portfolio.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_skills() -> list[dict]:
    """
    Retrieve the complete list of technical skills.

    Returns:
        list[dict]: Technical skills grouped by category.
    """
    return [
        {
            "name": "FastAPI",
            "category": "Backend",
        },
        {
            "name": "PostgreSQL",
            "category": "Database",
        },
        {
            "name": "Docker",
            "category": "DevOps",
        },
        {
            "name": "Pandas",
            "category": "Data",
        },
    ]