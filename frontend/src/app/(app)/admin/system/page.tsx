'use client'

import { useState } from 'react'
import { useTranslations } from 'next-intl'
import { Loader2, ShieldAlert } from 'lucide-react'
import { AdminNav } from '@/components/admin/AdminNav'
import { AdminPageHeader } from '@/components/admin/AdminShell'
import { apiFetch } from '@/lib/api'
import { useConfigStore } from '@/store/config'

export default function AdminSystemPage() {
  const t = useTranslations('admin')
  const maintenanceMode = useConfigStore((s) => s.maintenanceMode)
  const [maintenanceLoading, setMaintenanceLoading] = useState(false)
  const [error, setError] = useState('')

  async function toggleMaintenance() {
    setMaintenanceLoading(true)
    setError('')
    try {
      const nextMode = !maintenanceMode
      const res = await apiFetch('/api/admin/maintenance', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ maintenance_mode: nextMode }),
      })
      if (res.ok) {
        const data = await res.json()
        useConfigStore.setState({ maintenanceMode: data.maintenance_mode })
      } else {
        setError(t('maintenanceError'))
      }
    } catch {
      setError(t('maintenanceError'))
    } finally {
      setMaintenanceLoading(false)
    }
  }

  return (
    <div className="mx-auto max-w-6xl space-y-4 p-6">
      <AdminPageHeader
        eyebrow={`${t('title')} / ${t('system')}`}
        title={t('system')}
      />

      <AdminNav />

      {error && (
        <div className="border-fl-error/40 text-fl-error border px-4 py-3 font-mono text-xs">
          {error}
        </div>
      )}

      <div
        className={`border px-5 py-4 ${maintenanceMode ? 'border-yellow-500/40 bg-yellow-500/5' : 'border-fl-border bg-fl-surface'}`}
      >
        <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
          <div className="flex gap-3">
            <ShieldAlert
              className={`mt-0.5 size-5 shrink-0 ${maintenanceMode ? 'text-yellow-500' : 'text-fl-muted-3'}`}
              aria-hidden="true"
            />
            <div>
              <div className="mb-1 flex flex-wrap items-center gap-2">
                <span className="text-fl-muted-1 font-mono text-xs tracking-widest uppercase">
                  {t('maintenanceTitle')}
                </span>
                <span
                  className={`text-fl-hint border px-2 py-0.5 font-mono tracking-widest uppercase ${
                    maintenanceMode
                      ? 'border-yellow-500/40 text-yellow-500'
                      : 'border-fl-border text-fl-muted-3'
                  }`}
                >
                  {maintenanceMode ? t('maintenanceOn') : t('maintenanceOff')}
                </span>
              </div>
              <p className="text-fl-hint text-fl-muted-2 font-mono">
                {t('maintenanceDesc')}
              </p>
            </div>
          </div>
          <button
            onClick={toggleMaintenance}
            disabled={maintenanceLoading}
            className={`inline-flex shrink-0 items-center justify-center gap-2 px-4 py-3 font-mono text-xs font-bold tracking-widest uppercase transition-colors ${
              maintenanceMode
                ? 'bg-fl-fg text-fl-bg hover:bg-fl-fg/90'
                : 'bg-fl-accent text-fl-accent-fg hover:bg-fl-accent/90'
            } disabled:opacity-50`}
          >
            {maintenanceLoading && (
              <Loader2 className="size-3.5 animate-spin" aria-hidden="true" />
            )}
            {maintenanceMode ? t('maintenanceDisable') : t('maintenanceEnable')}
          </button>
        </div>
      </div>
    </div>
  )
}
