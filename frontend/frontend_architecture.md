# Portfolio SaaS Frontend Architecture

## Vision

The portfolio should feel like a professional SaaS dashboard rather than a traditional personal portfolio.

The objective is not to showcase frontend design skills, but to communicate backend engineering, data analytics, system design, and software architecture capabilities.

The experience should feel inspired by:

* Vercel
* Supabase
* Stripe
* Linear
* Grafana

The design language should be:

* Professional
* Technical
* Minimal
* Data-Oriented
* Modern

The portfolio should tell a vertical story through scrolling.

---

# User Journey

The user should naturally answer the following questions while scrolling:

1. Who is Alejandro?
2. What does he know?
3. What has he built?
4. What is he currently doing?
5. How does he think as an engineer?

---

# Page Structure

## Hero

### Purpose

Introduce the developer in less than five seconds.

### Layout

Two-column layout.

Left side:

* Name
* Title
* Short description
* Technical badges

Right side:

* Professional portrait or avatar

### Content

Name:

Alejandro Gabriel Pérez Muñoz

Title:

Backend Developer & Data Engineering Enthusiast

Description:

Building backend systems, data pipelines, and event-driven applications.

Technical badges:

* Python
* FastAPI
* PostgreSQL
* Docker
* RabbitMQ

Bottom section:

* "Explore Dashboard" button
* Down-arrow indicator

### Data Source

GET /api/v1/profile

---

# Engineering Overview

### Purpose

Provide a high-level technical summary.

### Layout

Metrics cards on top.

Technical capabilities below.

### Metrics

Projects

Programming Languages

Databases

Current Roles

### Skills

Grouped by category.

Backend

* Python
* Java
* Go
* TypeScript

Databases

* PostgreSQL
* Neo4j
* Supabase

Data

* Celonis
* Process Mining
* Data Integration

DevOps

* Docker
* RabbitMQ
* Git

Frameworks

* FastAPI
* Spring Boot

### Data Sources

GET /api/v1/metrics

GET /api/v1/skills

---

# Featured Projects

### Purpose

Showcase the strongest technical work.

### Layout

Project cards styled as software products or services.

Not colorful portfolio cards.

Each project should feel like a deployable system.

### Project Structure

Project title

Description

Technology stack

Features

GitHub link

### Featured Projects

Intent Classification System

Series Recommendation System

WhereNow

Portfolio SaaS

### Data Source

GET /api/v1/projects

---

# Development Activity

### Purpose

Show recent technical activity and engineering growth.

### Layout

Two-column section.

Left:

Activity timeline.

Right:

GitHub analytics.

### Timeline

Internship

Teaching Assistant

Completed Projects

Portfolio Development

### Analytics

Repositories

Commits

Pull Requests

Stars

### Data Sources

GET /api/v1/events

GET /api/v1/github-metrics

---

# How This Site Works

### Purpose

Demonstrate engineering thinking.

This section is intended for technical recruiters and engineers.

### Layout

Architecture diagram.

### Architecture

React
↓
FastAPI
↓
PostgreSQL

### Topics

Frontend

* React
* TypeScript
* Vite

Backend

* FastAPI
* Services Layer
* Dependency Injection

Database

* PostgreSQL
* SQLModel

Documentation

* Swagger
* OpenAPI

Architecture

* Project/Technology relationships
* Event tracking
* Metrics system

---

# Navigation

Sticky top navigation.

Sections:

* Home
* Overview
* Projects
* Activity
* Architecture

Navigation should smoothly scroll to each section.

---

# Animations

Animations should be subtle.

Allowed:

* Fade-in sections
* Smooth scrolling
* Hover effects
* Card transitions
* Counter animations

Avoid:

* 3D scenes
* Particle systems
* Heavy parallax
* Decorative motion unrelated to content

The portfolio should feel like an engineering dashboard, not a design showcase.

---

# Backend Integration

All portfolio content must come from the backend API.

Frontend should not contain hardcoded portfolio information.

Profile:

GET /api/v1/profile

Skills:

GET /api/v1/skills

Projects:

GET /api/v1/projects

Events:

GET /api/v1/events

Metrics:

GET /api/v1/metrics

GitHub Analytics:

GET /api/v1/github-metrics

---

# Final Goal

The visitor should leave with the impression that:

* Alejandro builds real systems.
* Alejandro understands backend architecture.
* Alejandro works comfortably with data.
* Alejandro thinks about scalability and maintainability.
* Alejandro can explain how his systems work.
