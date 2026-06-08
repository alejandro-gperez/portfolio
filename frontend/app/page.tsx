import { SiteNav } from "@/components/site-nav"
import { Hero } from "@/components/hero"
import { Overview } from "@/components/overview"
import { Projects } from "@/components/projects"
import { Activity } from "@/components/activity"
import { Architecture } from "@/components/architecture"
import { SiteFooter } from "@/components/site-footer"

export default function Page() {
  return (
    <div className="min-h-screen bg-background">
      <SiteNav />
      <main>
        <Hero />
        <Overview />
        <Projects />
        <Activity />
        <Architecture />
      </main>
      <SiteFooter />
    </div>
  )
}
