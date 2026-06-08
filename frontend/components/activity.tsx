import { Counter } from "@/components/counter"
import { Reveal } from "@/components/reveal"
import { SectionHeader } from "@/components/section-header"
import { timeline, githubMetrics, contributionGrid } from "@/lib/portfolio"
import { GitCommit, Rocket, Hammer, Briefcase } from "lucide-react"

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

export function Activity() {
  return (
    <section id="activity" className="border-b border-border py-20 md:py-28">
      <div className="mx-auto max-w-6xl px-5">
        <SectionHeader
          index="03"
          eyebrow="Development Activity"
          title="A live feed of the work"
          description="Recent roles and shipped systems on the left, repository engineering metrics on the right."
        />

        <div className="grid gap-6 lg:grid-cols-[1.1fr_1fr]">
          {/* timeline */}
          <Reveal>
            <div className="h-full rounded-xl border border-border bg-card p-6">
              <div className="mb-5 flex items-center gap-2 font-mono text-xs text-muted-foreground">
                <span className="size-2 animate-pulse rounded-full bg-chart-2" />
                activity.log
              </div>
              <ol className="relative">
                {timeline.map((item, i) => {
                  const Icon = typeIcon[item.type] ?? GitCommit
                  const last = i === timeline.length - 1
                  return (
                    <li key={item.title} className="relative flex gap-4 pb-6 last:pb-0">
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
                          <h3 className="text-sm font-medium text-foreground">{item.title}</h3>
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

          {/* github analytics */}
          <Reveal delay={120}>
            <div className="flex h-full flex-col gap-5 rounded-xl border border-border bg-card p-6">
              <div className="flex items-center gap-2 font-mono text-xs text-muted-foreground">
                <GitCommit className="size-3.5" />
                github_metrics.json
              </div>

              <div className="grid grid-cols-2 gap-4">
                {githubMetrics.map((m) => (
                  <div key={m.label} className="rounded-lg border border-border bg-secondary/40 p-4">
                    <div className="text-3xl font-semibold tracking-tight text-foreground">
                      <Counter value={m.value} suffix={m.suffix} />
                    </div>
                    <div className="mt-1 font-mono text-xs text-muted-foreground">{m.label}</div>
                  </div>
                ))}
              </div>

              <div className="mt-auto rounded-lg border border-border bg-secondary/40 p-4">
                <div className="mb-3 font-mono text-xs text-muted-foreground">
                  contribution density
                </div>
                <div className="flex gap-1.5">
                  {contributionGrid.map((week, wi) => (
                    <div key={wi} className="flex flex-col gap-1.5">
                      {week.map((level, di) => (
                        <span
                          key={di}
                          className={`size-3.5 rounded-sm ${cellShade[level]}`}
                          title={`${level} contributions`}
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
      </div>
    </section>
  )
}
