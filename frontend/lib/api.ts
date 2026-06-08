const API_BASE =
  "http://localhost:8000/api/v1"

export interface Metric {
  name: string
  value: number
  unit?: string | null
}

export interface Skill {
  name: string
  category: string
  level: number
}

export async function getMetrics(): Promise<Metric[]> {
  const response = await fetch(
    `${API_BASE}/metrics`
  )

  if (!response.ok) {
    throw new Error(
      "Failed to fetch metrics"
    )
  }

  return response.json()
}

export async function getSkills(): Promise<Skill[]> {
  const response = await fetch(
    `${API_BASE}/skills`
  )

  if (!response.ok) {
    throw new Error(
      "Failed to fetch skills"
    )
  }

  return response.json()
}

export interface Project {
  id: number
  name: string
  description: string
  status: string
  featured: boolean
  github_url: string | null
  demo_url: string | null
  stack: string[]
  features: {
    name: string
  }[]
}

export async function getProjects(): Promise<Project[]> {
  const response = await fetch(
    `${API_BASE}/projects`
  )

  if (!response.ok) {
    throw new Error(
      "Failed to fetch projects"
    )
  }

  return response.json()
}

export interface Event {
  event_type: string
  description: string
  created_at: string
}

export interface GitHubMetric {
  metric_name: string
  metric_value: number
}

export async function getEvents(): Promise<Event[]> {
  const response = await fetch(
    `${API_BASE}/events`
  )

  if (!response.ok) {
    throw new Error(
      "Failed to fetch events"
    )
  }

  return response.json()
}

export async function getGitHubMetrics(): Promise<
  GitHubMetric[]
> {
  const response = await fetch(
    `${API_BASE}/github-metrics`
  )

  if (!response.ok) {
    throw new Error(
      "Failed to fetch GitHub metrics"
    )
  }

  return response.json()
}

export interface Profile {
  name: string
  title: string
  bio: string
  github_url: string
  linkedin_url: string
  email: string
  location: string
  profile_image_url: string | null
}

export async function getProfile(): Promise<Profile> {
  const response = await fetch(
    `${API_BASE}/profile`
  )

  if (!response.ok) {
    throw new Error(
      "Failed to fetch profile"
    )
  }

  return response.json()
}