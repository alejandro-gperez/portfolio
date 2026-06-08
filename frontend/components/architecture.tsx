import { Reveal } from "@/components/reveal"
import { SectionHeader } from "@/components/section-header"
import { ArrowDown, Code2, Server, Database, FileJson, Network } from "lucide-react"

const flow = [
  {
    label: "React",
    sub: "TypeScript · Next.js",
    icon: Code2,
    note: "Renders the dashboard UI and emits client events.",
  },
  {
    label: "FastAPI",
    sub: "Services · Dependency Injection",
    icon: Server,
    note: "Handles requests through a clean services layer with injected dependencies.",
  },
  {
    label: "PostgreSQL",
    sub: "SQLModel",
    icon: Database,
    note: "Persists projects, technologies, events, and computed metrics.",
  },
]

const stack = [
  {
    title: "Frontend",
    icon: Code2,
    items: ["React", "TypeScript", "Next.js"],
  },
  {
    title: "Backend",
    icon: Server,
    items: ["FastAPI", "Services Layer", "Dependency Injection"],
  },
  {
    title: "Database",
    icon: Database,
    items: ["PostgreSQL", "SQLModel"],
  },
  {
    title: "Documentation",
    icon: FileJson,
    items: ["Swagger", "OpenAPI"],
  },
  {
    title: "Architecture",
    icon: Network,
    items: ["Project–Technology relations", "Event Tracking", "Metrics System"],
  },
]

export function Architecture() {
  return (
    <section id="architecture" className="py-20 md:py-28">
      <div className="mx-auto max-w-6xl px-5">
        <SectionHeader
          index="04"
          eyebrow="How This Site Works"
          title="A public architecture review"
          description="This site is itself a system. Here is the data flow and the stack behind every section you just scrolled through."
        />

        <div className="grid gap-6 lg:grid-cols-[1fr_1.2fr]">
          {/* diagram */}
          <Reveal>
            <div className="h-full rounded-xl border border-border bg-card p-6">
              <div className="mb-6 font-mono text-xs text-muted-foreground">data_flow.diagram</div>
              <div className="flex flex-col items-stretch gap-3">
                {flow.map((node, i) => {
                  const Icon = node.icon
                  return (
                    <div key={node.label}>
                      <div className="rounded-lg border border-border bg-secondary/40 p-4">
                        <div className="flex items-center gap-3">
                          <span className="flex size-9 items-center justify-center rounded-md bg-primary text-primary-foreground">
                            <Icon className="size-4" />
                          </span>
                          <div>
                            <div className="font-mono text-sm font-medium text-foreground">
                              {node.label}
                            </div>
                            <div className="font-mono text-[11px] text-muted-foreground">
                              {node.sub}
                            </div>
                          </div>
                        </div>
                        <p className="mt-3 text-sm leading-relaxed text-muted-foreground">
                          {node.note}
                        </p>
                      </div>
                      {i < flow.length - 1 && (
                        <div className="flex justify-center py-1.5">
                          <ArrowDown className="size-4 text-muted-foreground" />
                        </div>
                      )}
                    </div>
                  )
                })}
              </div>
            </div>
          </Reveal>

          {/* stack breakdown */}
          <Reveal delay={120}>
            <div className="grid h-full gap-4 sm:grid-cols-2">
              {stack.map((layer) => {
                const Icon = layer.icon
                return (
                  <div
                    key={layer.title}
                    className="rounded-xl border border-border bg-card p-5 last:sm:col-span-2"
                  >
                    <div className="mb-3 flex items-center gap-2.5">
                      <span className="flex size-8 items-center justify-center rounded-md bg-secondary text-primary">
                        <Icon className="size-4" />
                      </span>
                      <h3 className="font-mono text-sm font-medium text-foreground">
                        {layer.title}
                      </h3>
                    </div>
                    <ul className="flex flex-wrap gap-2">
                      {layer.items.map((item) => (
                        <li
                          key={item}
                          className="rounded-md border border-border bg-secondary/50 px-2.5 py-1 text-xs text-secondary-foreground"
                        >
                          {item}
                        </li>
                      ))}
                    </ul>
                  </div>
                )
              })}
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  )
}
