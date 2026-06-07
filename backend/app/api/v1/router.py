"""
API v1 router configuration.

This module aggregates all domain-specific routers and exposes
them under the /api/v1 prefix.

Keeping routers separated by domain entity improves maintainability,
scalability, and future API versioning.

"""

from fastapi import APIRouter

from app.api.v1.endpoints import (
    events,
    github_metrics,
    metrics,
    profile,
    projects,
    skills,
)

api_router = APIRouter()

# Profile endpoints
api_router.include_router(
    profile.router,
    prefix="/profile",
    tags=["Profile"],
)

# Skills endpoints
api_router.include_router(
    skills.router,
    prefix="/skills",
    tags=["Skills"],
)

# Projects endpoints
api_router.include_router(
    projects.router,
    prefix="/projects",
    tags=["Projects"],
)

# Dashboard metrics endpoints
api_router.include_router(
    metrics.router,
    prefix="/metrics",
    tags=["Metrics"],
)

# GitHub analytics endpoints
api_router.include_router(
    github_metrics.router,
    prefix="/github-metrics",
    tags=["GitHub Metrics"],
)

# Activity and event tracking endpoints
api_router.include_router(
    events.router,
    prefix="/events",
    tags=["Events"],
)