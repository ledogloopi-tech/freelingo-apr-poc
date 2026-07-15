'use client'

import { useEffect, useState } from 'react'
import { apiFetch } from '@/lib/api'
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'

type AprModuleMetadata = {
  module_id: string
  title: string
  status: string
  target_language: string
  bridge_language: string
  authorized_for_pilot: boolean
  authorized_for_public_release: boolean
}

const aprPocEnabled = process.env.NEXT_PUBLIC_APR_POC_ENABLED !== 'false'

export default function AprPrimeiraConexaoPage() {
  const [module, setModule] = useState<AprModuleMetadata | null>(null)
  const [loading, setLoading] = useState(aprPocEnabled)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (!aprPocEnabled) {
      setError('The APR technical proof of concept is disabled in this environment.')
      return
    }

    let active = true

    async function loadModule() {
      try {
        const res = await apiFetch('/api/apr/modules/primeira-conexao')
        if (!res.ok) {
          throw new Error(`APR API returned HTTP ${res.status}`)
        }
        const data = (await res.json()) as AprModuleMetadata
        if (active) setModule(data)
      } catch (err) {
        if (active) {
          setError(
            err instanceof Error
              ? `Technical error loading APR module metadata: ${err.message}`
              : 'Technical error loading APR module metadata.'
          )
        }
      } finally {
        if (active) setLoading(false)
      }
    }

    loadModule()

    return () => {
      active = false
    }
  }, [])

  return (
    <main className="mx-auto flex w-full max-w-3xl flex-1 flex-col px-4 py-6 sm:px-6 lg:py-10">
      <Card className="gap-6">
        <CardHeader>
          <Badge className="w-fit" variant="secondary">
            Technical proof of concept
          </Badge>
          <CardTitle className="text-2xl sm:text-3xl">
            Academia Português Reconectado
          </CardTitle>
          <CardDescription className="text-base">
            Primeira Conexão
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-6">
          <p className="text-muted-foreground">
            This page confirms that APR can operate as a separate product module
            inside the inherited FreeLingo infrastructure.
          </p>

          {loading && (
            <div role="status" className="rounded-lg border p-4 text-sm">
              Loading APR technical boundary metadata…
            </div>
          )}

          {error && (
            <div
              role="alert"
              className="rounded-lg border border-destructive/30 bg-destructive/10 p-4 text-sm text-destructive"
            >
              {error}
            </div>
          )}

          {module && !error && (
            <section className="rounded-lg border p-4" aria-label="APR metadata">
              <h2 className="font-heading text-lg font-semibold">
                {module.title}
              </h2>
              <dl className="mt-4 grid gap-3 text-sm sm:grid-cols-2">
                <div>
                  <dt className="font-medium">Module ID</dt>
                  <dd className="text-muted-foreground">{module.module_id}</dd>
                </div>
                <div>
                  <dt className="font-medium">Status</dt>
                  <dd className="text-muted-foreground">{module.status}</dd>
                </div>
              </dl>
            </section>
          )}

          <section aria-label="APR boundaries">
            <h2 className="font-heading text-lg font-semibold">Boundaries</h2>
            <ul className="mt-3 grid gap-2 text-sm sm:grid-cols-2">
              <li>Brazilian Portuguese: pt-BR</li>
              <li>Spanish bridge language: es</li>
              <li>No CEFR placement</li>
              <li>No XP or streak dependency</li>
              <li>No AI-generated curriculum</li>
              <li>Not authorized for pilot or public release</li>
            </ul>
          </section>
        </CardContent>
      </Card>
    </main>
  )
}
