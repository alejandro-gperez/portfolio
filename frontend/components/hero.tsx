"use client"

import Image from "next/image"
import { ArrowRight, ChevronDown, Circle } from "lucide-react"
import { GithubIcon } from "@/components/github-icon"
import { badges, GITHUB_URL } from "@/lib/portfolio"

export function Hero() {
  const scrollTo = (id: string) => {
    document.getElementById(id)?.scrollIntoView({ behavior: "smooth", block: "start" })
  }

  return (
    <section
      id="home"
      className="relative overflow-hidden border-b border-border pt-28 pb-20 md:pt-36 md:pb-28"
    >
      {/* subtle grid backdrop */}
      <div
        aria-hidden
        className="pointer-events-none absolute inset-0 opacity-[0.4]"
        style={{
          backgroundImage:
            "linear-gradient(to right, var(--border) 1px, transparent 1px), linear-gradient(to bottom, var(--border) 1px, transparent 1px)",
          backgroundSize: "56px 56px",
          maskImage: "radial-gradient(ellipse 80% 60% at 50% 0%, black 30%, transparent 80%)",
        }}
      />

      <div className="relative mx-auto grid max-w-6xl items-center gap-12 px-5 md:grid-cols-[1.25fr_1fr]">
        <div className="flex flex-col items-start">
          <div className="mb-6 inline-flex items-center gap-2 rounded-full border border-border bg-card px-3 py-1 font-mono text-xs text-muted-foreground">
            <Circle className="size-2 fill-chart-2 text-chart-2" />
            Available for backend & data engineering work
          </div>

          <h1 className="text-balance text-4xl font-semibold leading-[1.05] tracking-tight text-foreground md:text-6xl">
            Alejandro Gabriel
            <br />
            Pérez Muñoz
          </h1>

          <p className="mt-4 font-mono text-sm text-primary md:text-base">
            Backend Developer &amp; Data Engineering Enthusiast
          </p>

          <p className="mt-5 max-w-xl text-pretty text-base leading-relaxed text-muted-foreground">
            Building backend systems, data pipelines, and event-driven applications. I design
            architectures that move data reliably and explain how every piece fits together.
          </p>

          <ul className="mt-7 flex flex-wrap gap-2">
            {badges.map((b) => (
              <li
                key={b}
                className="rounded-md border border-border bg-card px-2.5 py-1 font-mono text-xs text-secondary-foreground"
              >
                {b}
              </li>
            ))}
          </ul>

          <div className="mt-8 flex flex-wrap items-center gap-3">
            <button
              onClick={() => scrollTo("overview")}
              className="group inline-flex items-center gap-2 rounded-md bg-primary px-5 py-2.5 text-sm font-medium text-primary-foreground transition-colors hover:bg-primary/90"
            >
              Explore Dashboard
              <ArrowRight className="size-4 transition-transform group-hover:translate-x-0.5" />
            </button>
            <a
              href={GITHUB_URL}
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center gap-2 rounded-md border border-border bg-card px-5 py-2.5 text-sm font-medium text-foreground transition-colors hover:bg-secondary"
            >
              <GithubIcon className="size-4" />
              View GitHub
            </a>
          </div>
        </div>

        {/* right: portrait card */}
        <div className="relative mx-auto w-full max-w-xs md:max-w-none">
          <div className="overflow-hidden rounded-xl border border-border bg-card shadow-sm">
            <div className="flex items-center justify-between border-b border-border bg-secondary/60 px-3 py-2">
              <div className="flex items-center gap-1.5">
                <span className="size-2.5 rounded-full bg-border" />
                <span className="size-2.5 rounded-full bg-border" />
                <span className="size-2.5 rounded-full bg-border" />
              </div>
              <span className="font-mono text-[11px] text-muted-foreground">profile.tsx</span>
            </div>
            <div className="relative aspect-[4/5] w-full">
              <Image
                src="/portrait.png"
                alt="Portrait of Alejandro Gabriel Pérez Muñoz"
                fill
                priority
                sizes="(max-width: 768px) 320px, 400px"
                className="object-cover"
              />
            </div>
            <div className="grid grid-cols-3 divide-x divide-border border-t border-border font-mono text-center text-[11px]">
              <div className="px-2 py-2.5">
                <div className="text-foreground">UTC-6</div>
                <div className="text-muted-foreground">timezone</div>
              </div>
              <div className="px-2 py-2.5">
                <div className="text-foreground">Backend</div>
                <div className="text-muted-foreground">focus</div>
              </div>
              <div className="px-2 py-2.5">
                <div className="text-chart-2">Online</div>
                <div className="text-muted-foreground">status</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <button
        onClick={() => scrollTo("overview")}
        aria-label="Scroll to overview"
        className="relative mx-auto mt-16 flex flex-col items-center gap-2 font-mono text-xs text-muted-foreground transition-colors hover:text-foreground"
      >
        scroll
        <ChevronDown className="size-4 animate-bounce" />
      </button>
    </section>
  )
}
