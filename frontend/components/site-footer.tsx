import { Terminal } from "lucide-react"
import { GithubIcon } from "@/components/github-icon"
import { GITHUB_URL } from "@/lib/portfolio"

export function SiteFooter() {
  return (
    <footer className="border-t border-border bg-card">
      <div className="mx-auto flex max-w-6xl flex-col items-center justify-between gap-4 px-5 py-8 sm:flex-row">
        <div className="flex items-center gap-2 font-mono text-sm text-muted-foreground">
          <Terminal className="size-4 text-primary" />
          Alejandro Gabriel Pérez Muñoz
        </div>
        <p className="font-mono text-xs text-muted-foreground">
          Designed &amp; engineered with React · FastAPI · PostgreSQL
        </p>
        <a
          href={GITHUB_URL}
          target="_blank"
          rel="noreferrer"
          className="inline-flex items-center gap-2 rounded-md border border-border px-3 py-1.5 text-sm text-foreground transition-colors hover:bg-secondary"
        >
          <GithubIcon className="size-4" />
          GitHub
        </a>
      </div>
    </footer>
  )
}
