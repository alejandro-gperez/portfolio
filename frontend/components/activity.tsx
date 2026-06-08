"use client"

/**
Development Activity section.

Displays:
Professional timeline.
GitHub engineering metrics.

Data is retrieved from the FastAPI backend.
*/

import { useEffect, useState } from "react"
import { GitCommit, Rocket, Hammer, Briefcase } from "lucide-react"
import { Counter } from "@/components/counter"
import { Reveal } from "@/components/reveal"
import { SectionHeader } from "@/components/section-header"
import { getEvents, getGitHubMetrics, type Event, type GitHubMetric } from "@/lib/api"

const typeIcon: Record<string, typeof GitCommit> = {
  role: Briefcase,
  deploy: Rocket,
  build: Hammer,
}

const cellShade = [
  "bg-secondary",
  "bg-chart-2/25",
  "bg-chart-2/45",
  "bg-chart-2/70",
  "bg-chart-2",
]

const contributionGrid: number[][] = [
  [0, 1, 2, 1, 0, 3, 2],
  [1, 2, 3, 2, 1, 0, 1],
  [2, 0, 1, 3, 4, 2, 1],
  [0, 1, 2, 4, 3, 1, 2],
  [3, 2, 1, 0, 2, 3, 4],
  [1, 0, 2, 3, 1, 2, 0],
  [2, 3, 4, 2, 1, 0, 1],
]

interface TimelineItem {
  title: string
  detail: string
  period: string
  type: string
}

export function Activity() {
  const [events, setEvents] = useState<Event[]>([])
  const [githubMetrics, setGithubMetrics] = useState<GitHubMetric[]>([])
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    async function loadData() {
      try {
        const [eventsData, githubData] = await Promise.all([
          getEvents(),
          getGitHubMetrics(),
        ])
        setEvents(eventsData)
        setGithubMetrics(githubData)
      } catch (error) {
        console.error("Failed to load activity data:", error)
      } finally {
        setIsLoading(false)
      }
    }

    loadData()
  }, [])

  const timeline: TimelineItem[] = events.map((event) => ({
    title: event.event_type.replaceAll("_", " "),
    detail: event.description,
    period: "Recent",
    type:
      event.event_type.includes("INTERNSHIP") || event.event_type.includes("ASSISTANT")
        ? "role"
        : "deploy",
  }))

  if (isLoading) {
    return (
      <div className="flex h-48 items-center justify-center font-mono text-sm text-muted-foreground">
        Loading activity data...
      </div>
    )
  }

  return (
    <section className="py-12">
      <SectionHeader title="Development Activity" description="Real-time engineering logs" />
      
      <div className="grid gap-6 lg:grid-cols-[1.1fr_1fr]">
        <Reveal>
          <div className="h-full rounded-xl border border-border bg-card p-6">
            <div className="mb-5 flex items-center gap-2 font-mono text-xs text-muted-foreground">
              <span className="size-2 animate-pulse rounded-full bg-chart-2" />
              activity.log
            </div>

            <ol className="relative">
              {timeline.map((item, index) => {
                const Icon = typeIcon[item.type] ?? GitCommit
                const last = index === timeline.length - 1

                return (
                  <li  key={`${item.title}-${index}`} className="relative flex gap-4 pb-6 last:pb-0">
                    {!last && (
                      <span
                        aria-hidden
                        className="absolute left-[15px] top-8 h-full w-px bg-border"
                      />
                    )}

                    <span className="relative z-10 flex size-8 shrink-0 items-center justify-center rounded-full border border-border bg-secondary text-primary">
                      <Icon className="size-4" />
                    </span>

                    <div className="pt-0.5">
                      <div className="flex items-center gap-2">
                        <h3 className="text-sm font-medium text-foreground">
                          {item.title}
                        </h3>
                        <span className="rounded border border-border px-1.5 py-0.5 font-mono text-[10px] text-muted-foreground">
                          {item.period}
                        </span>
                      </div>
                      <p className="mt-1 text-sm leading-relaxed text-muted-foreground">
                        {item.detail}
                      </p>
                    </div>
                  </li>
                )
              })}
            </ol>
          </div>
        </Reveal>

        <Reveal delay={120}>
          <div className="flex h-full flex-col gap-5 rounded-xl border border-border bg-card p-6">
            <div className="flex items-center gap-2 font-mono text-xs text-muted-foreground">
              <GitCommit className="size-3.5" />
              github_metrics.json
            </div>

            <div className="grid grid-cols-2 gap-4">
              {githubMetrics.map((metric) => (
                <div
                  key={metric.metric_name}
                  className="rounded-lg border border-border bg-secondary/40 p-4"
                >
                  <div className="text-3xl font-semibold tracking-tight text-foreground">
                    <Counter value={metric.metric_value} suffix="" />
                  </div>
                  <div className="mt-1 font-mono text-xs text-muted-foreground">
                    {metric.metric_name}
                  </div>
                </div>
              ))}
            </div>

            <div className="mt-auto rounded-lg border border-border bg-secondary/40 p-4">
              <div className="mb-3 font-mono text-xs text-muted-foreground">
                contribution density
              </div>

              <div className="flex gap-1.5">
                {contributionGrid.map((week, weekIndex) => (
                  <div key={weekIndex} className="flex flex-col gap-1.5">
                    {week.map((level, dayIndex) => (
                      <span
                        key={dayIndex}
                        className={`size-3.5 rounded-sm ${cellShade[level]}`}
                      />
                    ))}
                  </div>
                ))}

                <div className="ml-auto flex flex-col justify-end gap-1 font-mono text-[10px] text-muted-foreground">
                  <span>more</span>
                  <span className="size-3.5 rounded-sm bg-chart-2" />
                  <span className="size-3.5 rounded-sm bg-secondary" />
                  <span>less</span>
                </div>
              </div>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  )
}