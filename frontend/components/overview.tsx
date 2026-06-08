"use client"

/**
 * Engineering Overview section.
 *
 * Displays:
 * - High-level portfolio metrics.
 * - Categorized technical skills.
 *
 * Data is fetched directly from the FastAPI backend
 * instead of using hardcoded portfolio data.
 */

import { useEffect, useState } from "react"

import { Counter } from "@/components/counter"
import { Reveal } from "@/components/reveal"
import { SectionHeader } from "@/components/section-header"

import {
  getMetrics,
  getSkills,
  type Metric,
  type Skill,
} from "@/lib/api"

import {
  Database,
  Server,
  BarChart3,
  Boxes,
  Layers,
} from "lucide-react"

/**
 * Maps skill categories to icons.
 */
const groupIcons: Record<
  string,
  typeof Server
> = {
  Backend: Server,
  Database: Database,
  Data: BarChart3,
  DevOps: Boxes,
  Frameworks: Layers,
}

/**
 * Skill group representation used by the UI.
 */
interface SkillGroup {
  category: string
  items: string[]
}

export function Overview() {
  /**
   * Dashboard metrics retrieved from the backend.
   */
  const [metrics, setMetrics] =
    useState<Metric[]>([])

  /**
   * Technical skills retrieved from the backend.
   */
  const [skills, setSkills] =
    useState<Skill[]>([])

  /**
   * Loading state.
   */
  const [isLoading, setIsLoading] =
    useState(true)

  /**
   * Fetch metrics and skills on component mount.
   */
  useEffect(() => {
    async function loadData() {
      try {
        const [
          metricsData,
          skillsData,
        ] = await Promise.all([
          getMetrics(),
          getSkills(),
        ])

        setMetrics(metricsData)
        setSkills(skillsData)
      } catch (error) {
        console.error(
          "Failed to load overview data:",
          error
        )
      } finally {
        setIsLoading(false)
      }
    }

    loadData()
  }, [])

  /**
   * Group skills by category.
   *
   * Example:
   *
   * Backend:
   * - Python
   * - Java
   *
   * Database:
   * - PostgreSQL
   * - Neo4j
   */
  const skillGroups: SkillGroup[] =
    Object.entries(
      skills.reduce(
        (
          groups,
          skill
        ) => {
          if (
            !groups[
              skill.category
            ]
          ) {
            groups[
              skill.category
            ] = []
          }

          groups[
            skill.category
          ].push(skill.name)

          return groups
        },
        {} as Record<
          string,
          string[]
        >
      )
    ).map(
      ([category, items]) => ({
        category,
        items,
      })
    )

  return (
    <section
      id="overview"
      className="border-b border-border py-20 md:py-28"
    >
      <div className="mx-auto max-w-6xl px-5">
        <SectionHeader
          index="01"
          eyebrow="Engineering Overview"
          title="A snapshot of technical capability"
          description="The systems I build, the languages I work in, and the tools that move data from source to insight."
        />

        {/* ------------------------------------- */}
        {/* Loading State */}
        {/* ------------------------------------- */}

        {isLoading && (
          <div className="py-12 text-center text-sm text-muted-foreground">
            Loading engineering overview...
          </div>
        )}

        {!isLoading && (
          <>
            {/* ------------------------------------- */}
            {/* Metrics */}
            {/* ------------------------------------- */}

            <div className="grid grid-cols-2 gap-4 lg:grid-cols-4">
              {metrics.map(
                (
                  metric,
                  index
                ) => (
                  <Reveal
                    key={
                      metric.name
                    }
                    delay={
                      index * 80
                    }
                  >
                    <div className="rounded-lg border border-border bg-card p-5 transition-all hover:-translate-y-0.5 hover:shadow-sm">
                      <div className="font-mono text-xs uppercase tracking-wider text-muted-foreground">
                        {metric.name}
                      </div>

                      <div className="mt-3 text-4xl font-semibold tracking-tight text-foreground">
                        <Counter
                          value={
                            metric.value
                          }
                          suffix=""
                        />
                      </div>
                    </div>
                  </Reveal>
                )
              )}
            </div>

            {/* ------------------------------------- */}
            {/* Skill Categories */}
            {/* ------------------------------------- */}

            <div className="mt-6 grid gap-4 md:grid-cols-2 lg:grid-cols-3">
              {skillGroups.map(
                (
                  group,
                  index
                ) => {
                  const Icon =
                    groupIcons[
                      group.category
                    ] ??
                    Layers

                  return (
                    <Reveal
                      key={
                        group.category
                      }
                      delay={
                        index *
                        70
                      }
                    >
                      <div className="h-full rounded-lg border border-border bg-card p-5">
                        <div className="mb-4 flex items-center gap-2.5">
                          <span className="flex size-8 items-center justify-center rounded-md bg-secondary text-primary">
                            <Icon className="size-4" />
                          </span>

                          <h3 className="font-mono text-sm font-medium text-foreground">
                            {
                              group.category
                            }
                          </h3>
                        </div>

                        <ul className="flex flex-wrap gap-2">
                          {group.items.map(
                            (
                              item
                            ) => (
                              <li
                                key={
                                  item
                                }
                                className="rounded-md border border-border bg-secondary/50 px-2.5 py-1 text-xs text-secondary-foreground"
                              >
                                {item}
                              </li>
                            )
                          )}
                        </ul>
                      </div>
                    </Reveal>
                  )
                }
              )}
            </div>
          </>
        )}
      </div>
    </section>
  )
}