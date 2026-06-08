"""
Portfolio API application entrypoint.

This module initializes the FastAPI application and registers
all API routes exposed by the portfolio backend.

The application follows a versioned API strategy in order to
support future iterations without breaking existing consumers.
"""

from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import settings

from contextlib import asynccontextmanager
from app.core.database import create_db_and_tables

from fastapi.middleware.cors import CORSMiddleware

# ------------------------------------------------------------------
# Application Initialization
# ------------------------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup lifecycle.
    """
    create_db_and_tables()
    yield

app = FastAPI(
    lifespan=lifespan,
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.VERSION,
)

# --------------------------------------------------
# Cross-Origin Resource Sharing (CORS)
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://portfolio-one-sandy-40.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------------------------
# API Routing
# ------------------------------------------------------------------

# All version 1 endpoints are mounted under /api/v1.
# This makes future API versioning straightforward and predictable.
app.include_router(
    api_router,
    prefix=settings.API_V1_PREFIX,
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

