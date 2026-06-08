# Portfolio SaaS | Alejandro Gabriel Pérez Muñoz

## Live Deployment

**Portfolio:**
https://portfolio-one-sandy-40.vercel.app/

---

## Overview

This project is a full-stack portfolio platform designed to showcase software engineering projects, technical skills, professional experience, and system architecture through a data-driven approach.

Instead of building a traditional static portfolio, I chose to build the portfolio itself as a software product. Every section of the site is powered by a backend API, a PostgreSQL database, and a deployment pipeline similar to what would be used in a real production environment.

The goal was to demonstrate not only frontend design, but also backend architecture, data modeling, API design, containerization, deployment, and integration with external services.

---

## Architecture

```text
Browser
│
▼
Next.js Frontend (Vercel)
│
▼
FastAPI Backend (Render)
│
▼
PostgreSQL (Neon)
│
▼
GitHub Analytics Pipeline
```

---

## Technology Stack

### Frontend

* Next.js
* React
* TypeScript
* TailwindCSS
* Vercel

### Backend

* FastAPI
* SQLModel
* PostgreSQL
* Pydantic
* Uvicorn

### Infrastructure

* Docker
* Docker Compose
* Render
* Neon

### External Integrations

* GitHub REST API
* GitHub Personal Access Token Authentication

---

## Backend Design

The backend follows a layered architecture:

```text
API Layer
│
▼
Service Layer
│
▼
Data Layer
│
▼
PostgreSQL
```

### API Layer

Responsible for exposing REST endpoints.

Examples:

```text
/api/v1/profile
/api/v1/projects
/api/v1/skills
/api/v1/events
/api/v1/github-metrics
```

### Service Layer

Business logic is isolated from routing logic.

Examples:

```text
ProfileService
ProjectService
SkillService
GitHubService
GitHubMetricService
GitHubLanguageService
```

This keeps endpoints thin and makes the application easier to maintain and test.

### Data Layer

SQLModel was chosen to combine:

* SQLAlchemy ORM
* Pydantic validation

into a single modeling approach.

---

## Frontend Design

The frontend follows a component-based architecture.

Major sections:

```text
Hero
Overview
Projects
Activity
Architecture
```

Rather than hardcoding content, each section consumes backend endpoints and renders dynamic data.

Examples:

```text
Profile → /profile
Projects → /projects
Skills → /skills
Events → /events
Metrics → /metrics
```

This allows the portfolio to evolve without changing frontend code.

---

## GitHub Analytics Pipeline

One of the most interesting features of the project is the GitHub analytics integration.

A synchronization script fetches information from the GitHub API and stores it inside PostgreSQL.

Pipeline:

```text
GitHub API
│
▼
GitHubService
│
▼
sync_github_metrics.py
│
▼
PostgreSQL
│
▼
REST API
│
▼
Frontend Dashboard
```

The frontend never talks directly to GitHub.

Instead:

```text
GitHub
↓
Backend
↓
Database
↓
Frontend
```

This approach resembles a real analytics pipeline.

---

## Dockerization

The backend was containerized using Docker and Docker Compose.

Services:

```text
FastAPI
PostgreSQL
```

Development environment:

```bash
docker compose up --build
```

This guarantees environment consistency and mirrors production deployment.

---

## Running Locally

### Backend

```bash
cd backend

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

API Documentation:

```text
http://localhost:8000/docs
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```text
http://localhost:3000
```

---

## Reflection

### Target Audience

This portfolio is primarily aimed at technical recruiters, software engineering internship programs, backend engineering roles, and data engineering opportunities.

Instead of emphasizing visual design alone, the project highlights architecture, APIs, databases, deployment, and system design decisions.

The intended message is:

> I can design, build, deploy, and maintain complete software systems.

---

### Technologies Chosen and Why

FastAPI was selected because it provides excellent developer productivity, automatic OpenAPI documentation, and strong typing through Pydantic.

PostgreSQL was chosen because it is a production-grade relational database commonly used in industry.

SQLModel was selected because it combines the strengths of SQLAlchemy and Pydantic into a unified development experience.

Next.js and React were chosen because they are widely adopted in modern web development and integrate naturally with API-driven architectures.

Docker was used to guarantee consistent environments across development and deployment.

Neon and Render were selected because they provide managed PostgreSQL hosting and backend deployment with minimal operational overhead.

---

### Technology Not Used

One technology discussed during the course that I intentionally decided not to use was Vite as the final frontend platform.

During the design phase, the project initially started with a Vite-based setup and several generated frontend prototypes were explored using that approach. However, as the project evolved and deployment requirements became clearer, I migrated to Next.js.

The main reason was that Next.js provided a more complete production-oriented ecosystem, including a smoother deployment experience on Vercel, built-in optimization features, and a structure that scales better for larger frontend applications.

Although Vite offers excellent development speed and simplicity, I felt that Next.js aligned more closely with the long-term goals of the project and with the type of production environments I expect to work with professionally.

---

### Where I Took Risks

The largest risk was building the portfolio itself as a software product rather than a static website.

This introduced significantly more complexity:

* Database modeling
* API architecture
* GitHub integration
* Deployment pipelines
* Dockerization

However, it also allowed me to demonstrate backend engineering skills that a traditional portfolio could not showcase.

Another risk was implementing a GitHub analytics pipeline that synchronizes external data into PostgreSQL.

---

### Where I Played It Safe

I intentionally chose proven technologies that i had learned during the course or that i was already familiar with:

* FastAPI
* PostgreSQL
* React
* Docker

Rather than experimenting with newer frameworks, I prioritized maintainability, documentation quality, and industry relevance.

---

### What I Would Improve With One More Week

Given an additional week, I would focus on:

1. Automated GitHub metric synchronization through scheduled jobs.
2. CI/CD pipelines using GitHub Actions.
3. Unit and integration test coverage.
4. Custom domain configuration.
5. Observability dashboards and request metrics.
6. More advanced GitHub analytics visualizations.
7. Deployment with my own domain.

The current project already demonstrates full-stack engineering principles, but these additions would push it closer to a production-grade SaaS platform.

---

## Author

**Alejandro Gabriel Pérez Muñoz**

Backend Developer & Data Engineering Enthusiast

GitHub:
https://github.com/alejandro-gperez

LinkedIn:
https://www.linkedin.com/in/alejandro-gabriel-pérez-muñoz-3b664a394
