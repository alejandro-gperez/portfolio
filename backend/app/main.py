"""
Portfolio API application entrypoint.

This module initializes the FastAPI application and registers
all API routes exposed by the portfolio backend.

The application follows a versioned API strategy in order to
support future iterations without breaking existing consumers.
"""

from fastapi import FastAPI

from app.api.v1.router import api_router

# ------------------------------------------------------------------
# Application Initialization
# ------------------------------------------------------------------

app = FastAPI(
    title="Alejandro Portfolio API",
    description=(
        "Backend API powering the Portfolio SaaS platform. "
        "Provides profile information, project data, GitHub analytics, "
        "dashboard metrics, and activity tracking."
    ),
    version="1.0.0",
)

# ------------------------------------------------------------------
# API Routing
# ------------------------------------------------------------------

# All version 1 endpoints are mounted under /api/v1.
# This makes future API versioning straightforward and predictable.
app.include_router(
    api_router,
    prefix="/api/v1",
)

# ------------------------------------------------------------------
# Health / Root Endpoints
# ------------------------------------------------------------------


@app.get(
    "/",
    tags=["Root"],
    summary="Root endpoint",
)
def root() -> dict[str, str]:
    """
    Root endpoint used to verify that the API is running.

    Returns:
        dict[str, str]: Basic API status message.
    """
    return {
        "message": "Portfolio API running",
    }


@app.get(
    "/health",
    tags=["Health"],
    summary="Health check",
)
def health_check() -> dict[str, str]:
    """
    Health check endpoint.

    This endpoint is intended for uptime monitoring,
    load balancers, and deployment verification.

    Returns:
        dict[str, str]: Current application health status.
    """
    return {
        "status": "healthy",
    }