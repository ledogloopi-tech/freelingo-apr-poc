'use client'

import Link from 'next/link'
import { useEffect, useState } from 'react'
import { useTranslations } from 'next-intl'
import { apiFetch } from '@/lib/api'
import {
  getLastCheckoutPlan,
  saveLastCheckoutPlan,
  type BillingInterval,
} from '@/lib/billing-checkout'

export default function BillingCanceledPage() {
  const t = useTranslations('billing')
  const [plan, setPlan] = useState<BillingInterval>('yearly')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    setPlan(getLastCheckoutPlan() ?? 'yearly')
  }, [])

  async function retryCheckout() {
    setLoading(true)
    setError(null)
    try {
      saveLastCheckoutPlan(plan)
      const res = await apiFetch('/api/billing/checkout', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ plan }),
      })
      if (!res.ok) {
        const data = await res.json().catch(() => ({}))
        throw new Error(data.detail ?? t('checkoutError'))
      }
      const { url } = await res.json()
      window.location.assign(url)
    } catch (err) {
      setError(err instanceof Error ? err.message : t('checkoutError'))
      setLoading(false)
    }
  }

  const planName = t(plan === 'yearly' ? 'planYearlyName' : 'planMonthlyName')

  return (
    <div className="bg-fl-bg bg-dot-grid flex min-h-screen items-center justify-center px-4">
      <div className="border-fl-border bg-fl-surface w-full max-w-sm space-y-5 border p-8 text-center">
        <div className="text-fl-muted-2 text-2xl">△</div>
        <p className="text-fl-label text-fl-muted-2 font-mono tracking-widest uppercase">
          {t('canceledLabel')}
        </p>
        <h1 className="text-fl-fg font-mono text-base font-bold">
          {t('canceledTitle')}
        </h1>
        <p className="text-fl-muted-1 font-mono text-xs leading-relaxed">
          {t('canceledDesc')}
        </p>
        <div className="flex flex-col gap-2">
          <button
            type="button"
            onClick={retryCheckout}
            disabled={loading}
            className="bg-fl-accent text-fl-accent-fg hover:bg-fl-accent/90 block py-3 font-mono text-xs font-bold tracking-widest uppercase transition-colors"
          >
            {loading ? '...' : t('canceledCtaRetry', { plan: planName })}
          </button>
          <Link
            href="/dashboard"
            className="border-fl-border text-fl-muted-1 hover:text-fl-fg hover:border-fl-border-2 block border py-3 font-mono text-xs tracking-widest uppercase transition-colors"
          >
            {t('canceledCtaDashboard')}
          </Link>
        </div>
        {error && <p className="text-fl-error font-mono text-xs">{error}</p>}
        <p className="text-fl-hint text-fl-muted-3 font-mono tracking-widest uppercase">
          {t('canceledNoCharge')}
        </p>
      </div>
    </div>
  )
}
