import { Reveal } from "@/components/reveal"

export function SectionHeader({
  index,
  eyebrow,
  title,
  description,
}: {
  index: string
  eyebrow: string
  title: string
  description?: string
}) {
  return (
    <Reveal className="mb-12 max-w-2xl">
      <div className="mb-3 flex items-center gap-3 font-mono text-xs text-muted-foreground">
        <span className="text-primary">{index}</span>
        <span className="h-px w-8 bg-border" />
        <span className="uppercase tracking-widest">{eyebrow}</span>
      </div>
      <h2 className="text-balance text-3xl font-semibold tracking-tight text-foreground md:text-4xl">
        {title}
      </h2>
      {description ? (
        <p className="mt-3 text-pretty text-base leading-relaxed text-muted-foreground">
          {description}
        </p>
      ) : null}
    </Reveal>
  )
}
