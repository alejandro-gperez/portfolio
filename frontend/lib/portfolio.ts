export const GITHUB_URL = "https://github.com"

export const navItems = [
  { label: "Home", href: "#home" },
  { label: "Overview", href: "#overview" },
  { label: "Projects", href: "#projects" },
  { label: "Activity", href: "#activity" },
  { label: "Architecture", href: "#architecture" },
]

export const badges = ["Python", "FastAPI", "PostgreSQL", "Docker", "RabbitMQ"]

export const metrics = [
  { label: "Projects", value: 4, suffix: "", hint: "shipped systems" },
  { label: "Languages", value: 6, suffix: "", hint: "production-ready" },
  { label: "Databases", value: 3, suffix: "", hint: "SQL & graph" },
  { label: "Current Roles", value: 2, suffix: "", hint: "active" },
]

export const skillGroups = [
  {
    category: "Backend",
    items: ["Python", "Java", "Go", "TypeScript"],
  },
  {
    category: "Databases",
    items: ["PostgreSQL", "Neo4j", "Supabase"],
  },
  {
    category: "Data",
    items: ["Celonis", "Process Mining", "Data Integration"],
  },
  {
    category: "DevOps",
    items: ["Docker", "RabbitMQ", "Git"],
  },
  {
    category: "Frameworks",
    items: ["FastAPI", "Spring Boot"],
  },
]

export type Project = {
  id: string
  title: string
  status: string
  description: string
  features: string[]
  technologies: string[]
  github: string
}

export const projects: Project[] = [
  {
    id: "intent-classification",
    title: "Intent Classification System",
    status: "Production",
    description:
      "An event-driven NLP service that classifies user intents in real time using a fine-tuned DistilBERT model, processed asynchronously through message queue workers.",
    features: [
      "DistilBERT Fine-Tuning",
      "Event-Driven Architecture",
      "RabbitMQ Workers",
      "Asynchronous Processing",
      "Dockerized Services",
    ],
    technologies: ["Python", "Docker", "RabbitMQ", "Transformers"],
    github: GITHUB_URL,
  },
  {
    id: "series-recommendation",
    title: "Series Recommendation System",
    status: "Production",
    description:
      "A graph-based recommendation engine that surfaces personalized series suggestions through optimized Cypher queries exposed over a clean REST API.",
    features: [
      "Graph-Based Recommendations",
      "REST API",
      "Cypher Query Optimization",
      "Personalized Suggestions",
    ],
    technologies: ["Java", "Spring Boot", "Neo4j", "Angular"],
    github: GITHUB_URL,
  },
  {
    id: "wherenow",
    title: "WhereNow",
    status: "Mobile",
    description:
      "A real-time social mobile application built on a clean MVVM architecture, with Firebase authentication and live data synchronization.",
    features: ["MVVM Architecture", "Firebase Authentication", "Real-Time Data", "Social Features"],
    technologies: ["Kotlin", "Jetpack Compose", "Firebase"],
    github: GITHUB_URL,
  },
  {
    id: "portfolio-saas",
    title: "Portfolio SaaS",
    status: "Active",
    description:
      "The platform powering this site — a FastAPI backend with PostgreSQL persistence, event tracking, and GitHub analytics, fully documented with Swagger.",
    features: [
      "FastAPI Backend",
      "PostgreSQL",
      "Swagger Documentation",
      "Event Tracking",
      "GitHub Analytics",
    ],
    technologies: ["FastAPI", "PostgreSQL", "Docker", "React"],
    github: GITHUB_URL,
  },
]

export type TimelineItem = {
  title: string
  detail: string
  period: string
  type: string
}

export const timeline: TimelineItem[] = [
  {
    title: "Data Analyst & Process Mining Internship",
    detail: "Started analyzing operational data and building process intelligence with Celonis.",
    period: "Current",
    type: "role",
  },
  {
    title: "Teaching Assistant",
    detail: "Supporting students in software engineering and data structures coursework.",
    period: "Current",
    type: "role",
  },
  {
    title: "Developed Intent Classification System",
    detail: "Shipped an event-driven NLP service with RabbitMQ workers and DistilBERT.",
    period: "Recent",
    type: "deploy",
  },
  {
    title: "Built Recommendation Engine",
    detail: "Designed a graph-based recommendation system on Neo4j and Spring Boot.",
    period: "Recent",
    type: "deploy",
  },
  {
    title: "Started Portfolio SaaS",
    detail: "Began building the FastAPI + PostgreSQL platform behind this site.",
    period: "Recent",
    type: "build",
  },
]

export const githubMetrics = [
  { label: "Repositories", value: 38, suffix: "" },
  { label: "Commits", value: 1240, suffix: "" },
  { label: "Pull Requests", value: 96, suffix: "" },
  { label: "Stars", value: 210, suffix: "" },
]

// 7 weeks x 7 days contribution intensity grid (0-4)
export const contributionGrid: number[][] = [
  [0, 1, 2, 1, 0, 3, 2],
  [1, 2, 3, 2, 1, 0, 1],
  [2, 0, 1, 3, 4, 2, 1],
  [0, 1, 2, 4, 3, 1, 2],
  [3, 2, 1, 0, 2, 3, 4],
  [1, 0, 2, 3, 1, 2, 0],
  [2, 3, 4, 2, 1, 0, 1],
]
