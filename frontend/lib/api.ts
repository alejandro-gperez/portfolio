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