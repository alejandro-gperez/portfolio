"use client"

/**
 * Featured Projects section.
 *
 * Displays portfolio projects retrieved from the backend API.
 *
 * Each project represents a real system and showcases:
 * - Description
 * - Features
 * - Technology stack
 * - Repository link
 */

import { useEffect, useState } from "react"

import {
  ArrowUpRight,
  Check,
  GitBranch,
} from "lucide-react"

import { Reveal } from "@/components/reveal"
import { SectionHeader } from "@/components/section-header"

import {
  getProjects,
  type Project,
} from "@/lib/api"

/**
 * Visual styles for project status badges.
 */
const statusStyles: Record<
  string,
  string
> = {
  Completed:
    "bg-chart-2/15 text-chart-2 border-chart-2/30",

  "In Progress":
    "bg-primary/10 text-primary border-primary/25",

  Mobile:
    "bg-accent text-accent-foreground border-border",
}

export function Projects() {
  /**
   * Projects retrieved from FastAPI.
   */
  const [projects, setProjects] =
    useState<Project[]>([])

  /**
   * Loading state.
   */
  const [isLoading, setIsLoading] =
    useState(true)

  /**
   * Load projects on component mount.
   */
  useEffect(() => {
    async function loadProjects() {
      try {
        const data =
          await getProjects()

        setProjects(data)
      } catch (error) {
        console.error(
          "Failed to load projects:",
          error
        )
      } finally {
        setIsLoading(false)
      }
    }

    loadProjects()
  }, [])

  /**
   * Loading UI.
   */
  if (isLoading) {
    return (
      <section
        id="projects"
        className="border-b border-border py-20 md:py-28"
      >
        <div className="mx-auto max-w-6xl px-5">
          <SectionHeader
            index="02"
            eyebrow="Featured Projects"
            title="Systems, not screenshots"
            description="Loading projects..."
          />
        </div>
      </section>
    )
  }

  return (
    <section
      id="projects"
      className="border-b border-border py-20 md:py-28"
    >
      <div className="mx-auto max-w-6xl px-5">
        <SectionHeader
          index="02"
          eyebrow="Featured Projects"
          title="Systems, not screenshots"
          description="Each project is presented as a deployable system — its stack, its capabilities, and where to read the source."
        />

        <div className="grid gap-5 md:grid-cols-2">
          {projects.map(
            (
              project,
              index
            ) => (
              <Reveal
                as="article"
                key={project.id}
                delay={
                  (index % 2) *
                  90
                }
              >
                <div className="group flex h-full flex-col rounded-xl border border-border bg-card transition-all hover:-translate-y-1 hover:shadow-md">
                  {/* Header */}

                  <div className="flex items-start justify-between gap-4 border-b border-border px-5 py-4">
                    <div className="flex items-center gap-2.5">
                      <span className="flex size-8 items-center justify-center rounded-md bg-secondary text-primary">
                        <GitBranch className="size-4" />
                      </span>

                      <h3 className="text-lg font-semibold tracking-tight text-foreground">
                        {project.name}
                      </h3>
                    </div>

                    <span
                      className={`shrink-0 rounded-full border px-2.5 py-0.5 font-mono text-[11px] ${
                        statusStyles[
                          project.status
                        ] ??
                        "border-border bg-secondary text-muted-foreground"
                      }`}
                    >
                      {project.status}
                    </span>
                  </div>

                  {/* Content */}

                  <div className="flex flex-1 flex-col gap-5 p-5">
                    <p className="text-sm leading-relaxed text-muted-foreground">
                      {
                        project.description
                      }
                    </p>

                    {/* Features */}

                    <div>
                      <div className="mb-2 font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
                        Features
                      </div>

                      <ul className="grid gap-1.5 sm:grid-cols-2">
                        {project.features.map(
                          (
                            feature
                          ) => (
                            <li
                              key={
                                feature.name
                              }
                              className="flex items-center gap-2 text-sm text-foreground"
                            >
                              <Check className="size-3.5 shrink-0 text-chart-2" />

                              {
                                feature.name
                              }
                            </li>
                          )
                        )}
                      </ul>
                    </div>

                    {/* Stack */}

                    <div className="mt-auto">
                      <div className="mb-2 font-mono text-[11px] uppercase tracking-wider text-muted-foreground">
                        Stack
                      </div>

                      <div className="flex flex-wrap gap-2">
                        {project.stack.map(
                          (
                            technology
                          ) => (
                            <span
                              key={
                                technology
                              }
                              className="rounded-md border border-border bg-secondary/50 px-2.5 py-1 font-mono text-xs text-secondary-foreground"
                            >
                              {
                                technology
                              }
                            </span>
                          )
                        )}
                      </div>
                    </div>
                  </div>

                  {/* Footer */}

                  <a
                    href={
                      project.github_url ??
                      "#"
                    }
                    target="_blank"
                    rel="noreferrer"
                    className="flex items-center justify-between border-t border-border px-5 py-3 text-sm font-medium text-foreground transition-colors hover:bg-secondary/60"
                  >
                    View repository

                    <ArrowUpRight className="size-4 text-muted-foreground transition-transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
                  </a>
                </div>
              </Reveal>
            )
          )}
        </div>
      </div>
    </section>
  )
}