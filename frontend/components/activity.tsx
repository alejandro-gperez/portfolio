"use client"

/**
 * Development Activity section.
 *
 * Displays:
 * - Professional timeline.
 * - GitHub engineering metrics.
 * - Technology footprint derived from featured projects.
 */

import { useEffect, useState } from "react"

import {
  GitCommit,
  Rocket,
  Briefcase,
} from "lucide-react"

import { Counter } from "@/components/counter"
import { Reveal } from "@/components/reveal"
import { SectionHeader } from "@/components/section-header"

import {
  getEvents,
  getGitHubMetrics,
  getProjects,
  type Event,
  type GitHubMetric,
  type Project,
} from "@/lib/api"

const typeIcon: Record<
  string,
  typeof GitCommit
> = {
  role: Briefcase,
  deploy: Rocket,
}

interface TimelineItem {
  title: string
  detail: string
  period: string
  type: string
}

export function Activity() {
  const [events, setEvents] =
    useState<Event[]>([])

  const [
    githubMetrics,
    setGithubMetrics,
  ] = useState<
    GitHubMetric[]
  >([])

  const [
    projects,
    setProjects,
  ] = useState<Project[]>([])

  const [isLoading, setIsLoading] =
    useState(true)

  useEffect(() => {
    async function loadData() {
      try {
        const [
          eventsData,
          githubData,
          projectsData,
        ] = await Promise.all([
          getEvents(),
          getGitHubMetrics(),
          getProjects(),
        ])

        setEvents(eventsData)

        setGithubMetrics(
          githubData
        )

        setProjects(
          projectsData
        )
      } catch (error) {
        console.error(
          "Failed to load activity data:",
          error
        )
      } finally {
        setIsLoading(false)
      }
    }

    loadData()
  }, [])

  /**
   * Transform backend events into timeline items.
   */
  const timeline: TimelineItem[] =
    events.map(
      (event) => ({
        title:
          event.event_type.replaceAll(
            "_",
            " "
          ),

        detail:
          event.description,

        period:
          "Recent",

        type:
          event.event_type.includes(
            "INTERNSHIP"
          ) ||
          event.event_type.includes(
            "ASSISTANT"
          )
            ? "role"
            : "deploy",
      })
    )

  /**
   * Build technology footprint
   * from featured projects.
   */
  const technologyFootprint =
    Object.entries(
      projects.reduce(
        (
          technologies,
          project
        ) => {
          project.stack.forEach(
            (
              technology
            ) => {
              technologies[
                technology
              ] =
                (
                  technologies[
                    technology
                  ] ?? 0
                ) + 1
            }
          )

          return technologies
        },
        {} as Record<
          string,
          number
        >
      )
    )
      .map(
        ([name, count]) => ({
          name,
          count,
        })
      )
      .sort(
        (a, b) =>
          b.count - a.count
      )

  if (isLoading) {
    return (
      <section
        id="activity"
        className="border-b border-border py-20 md:py-28"
      >
        <div className="mx-auto max-w-6xl px-5">
          <SectionHeader
            index="03"
            eyebrow="Development Activity"
            title="A live feed of the work"
            description="Loading activity..."
          />
        </div>
      </section>
    )
  }

  return (
    <section
      id="activity"
      className="border-b border-border py-20 md:py-28"
    >
      <div className="mx-auto max-w-6xl px-5">
        <SectionHeader
          index="03"
          eyebrow="Development Activity"
          title="A live feed of the work"
          description="Recent roles and shipped systems on the left, repository engineering metrics on the right."
        />

        <div className="grid gap-6 lg:grid-cols-[1.1fr_1fr]">
          {/* Timeline */}

          <Reveal>
            <div className="h-full rounded-xl border border-border bg-card p-6">
              <div className="mb-5 flex items-center gap-2 font-mono text-xs text-muted-foreground">
                <span className="size-2 animate-pulse rounded-full bg-chart-2" />
                activity.log
              </div>

              <ol className="relative">
                {timeline.map(
                  (
                    item,
                    index
                  ) => {
                    const Icon =
                      typeIcon[
                        item.type
                      ] ??
                      GitCommit

                    const last =
                      index ===
                      timeline.length -
                        1

                    return (
                      <li
                        key={`${item.title}-${index}`}
                        className="relative flex gap-4 pb-6 last:pb-0"
                      >
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
                  }
                )}
              </ol>
            </div>
          </Reveal>

          {/* GitHub Analytics */}

          <Reveal delay={120}>
            <div className="flex h-full flex-col gap-5 rounded-xl border border-border bg-card p-6">
              <div className="flex items-center gap-2 font-mono text-xs text-muted-foreground">
                <GitCommit className="size-3.5" />
                github_metrics.json
              </div>

              <div className="grid grid-cols-2 gap-4">
                {githubMetrics.map(
                  (
                    metric
                  ) => (
                    <div
                      key={
                        metric.metric_name
                      }
                      className="rounded-lg border border-border bg-secondary/40 p-4"
                    >
                      <div className="text-3xl font-semibold tracking-tight text-foreground">
                        <Counter
                          value={
                            metric.metric_value
                          }
                          suffix=""
                        />
                      </div>

                      <div className="mt-1 font-mono text-xs text-muted-foreground">
                        {
                          metric.metric_name
                        }
                      </div>
                    </div>
                  )
                )}
              </div>

              {/* Technology Footprint */}

              <div className="mt-auto rounded-lg border border-border bg-secondary/40 p-4">
                <div className="mb-3 font-mono text-xs text-muted-foreground">
                  technology_footprint.analytics
                </div>

                <div className="space-y-3">
                  {technologyFootprint
                    .slice(0, 8)
                    .map(
                      (
                        technology
                      ) => (
                        <div
                          key={
                            technology.name
                          }
                        >
                          <div className="mb-1 flex items-center justify-between text-xs">
                            <span>
                              {
                                technology.name
                              }
                            </span>

                            <span className="font-mono text-muted-foreground">
                              {(
                                (technology.count /
                                  projects.length) *
                                  100
                              ).toFixed(0)
                              }%
                            </span>
                          </div>

                          <div className="h-2 overflow-hidden rounded-full bg-secondary">
                            <div
                              className="h-full bg-primary"
                              style={{
                                width: `${(technology.count / projects.length) * 100}%`,
                              }}
                            />
                          </div>
                        </div>
                      )
                    )}
                </div>
              </div>
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  )
}