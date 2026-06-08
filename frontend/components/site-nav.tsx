"use client"

import { useEffect, useState } from "react"
import { Terminal } from "lucide-react"
import { GithubIcon } from "@/components/github-icon"
import { navItems, GITHUB_URL } from "@/lib/portfolio"
import { cn } from "@/lib/utils"

export function SiteNav() {
  const [active, setActive] = useState("home")
  const [scrolled, setScrolled] = useState(false)

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 8)
    onScroll()
    window.addEventListener("scroll", onScroll, { passive: true })
    return () => window.removeEventListener("scroll", onScroll)
  }, [])

  useEffect(() => {
    const ids = navItems.map((n) => n.href.slice(1))
    const sections = ids
      .map((id) => document.getElementById(id))
      .filter(Boolean) as HTMLElement[]
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) setActive(entry.target.id)
        })
      },
      { rootMargin: "-45% 0px -50% 0px", threshold: 0 },
    )
    sections.forEach((s) => observer.observe(s))
    return () => observer.disconnect()
  }, [])

  const handleClick = (e: React.MouseEvent, href: string) => {
    e.preventDefault()
    const el = document.getElementById(href.slice(1))
    if (el) el.scrollIntoView({ behavior: "smooth", block: "start" })
  }

  return (
    <header
      className={cn(
        "fixed inset-x-0 top-0 z-50 transition-all duration-300",
        scrolled
          ? "border-b border-border bg-background/80 backdrop-blur-md"
          : "border-b border-transparent",
      )}
    >
      <nav className="mx-auto flex h-16 max-w-6xl items-center justify-between px-5">
        <a
          href="#home"
          onClick={(e) => handleClick(e, "#home")}
          className="flex items-center gap-2 font-mono text-sm font-semibold tracking-tight text-foreground"
        >
          <span className="flex size-7 items-center justify-center rounded-md bg-primary text-primary-foreground">
            <Terminal className="size-4" />
          </span>
          <span>agpm</span>
          <span className="text-muted-foreground">/dev</span>
        </a>

        <ul className="hidden items-center gap-1 md:flex">
          {navItems.map((item) => {
            const id = item.href.slice(1)
            const isActive = active === id
            return (
              <li key={item.href}>
                <a
                  href={item.href}
                  onClick={(e) => handleClick(e, item.href)}
                  className={cn(
                    "rounded-md px-3 py-1.5 text-sm transition-colors",
                    isActive
                      ? "bg-secondary text-foreground"
                      : "text-muted-foreground hover:text-foreground",
                  )}
                >
                  {item.label}
                </a>
              </li>
            )
          })}
        </ul>

        <a
          href={GITHUB_URL}
          target="_blank"
          rel="noreferrer"
          className="flex items-center gap-2 rounded-md border border-border bg-card px-3 py-1.5 text-sm font-medium text-foreground transition-colors hover:bg-secondary"
        >
          <GithubIcon className="size-4" />
          <span className="hidden sm:inline">GitHub</span>
        </a>
      </nav>
    </header>
  )
}
