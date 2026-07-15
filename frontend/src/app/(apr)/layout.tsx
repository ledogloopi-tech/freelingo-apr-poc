'use client'

import { useEffect, useRef, useState } from 'react'
import { useRouter } from 'next/navigation'
import { apiFetch } from '@/lib/api'
import { mapUser } from '@/lib/mappers'
import { useAuthStore } from '@/store/auth'
import { PageLoading } from '@/components/ui/page-loading'

export default function AprLayout({ children }: { children: React.ReactNode }) {
  const router = useRouter()
  const accessToken = useAuthStore((s) => s.accessToken)
  const setTokens = useAuthStore((s) => s.setTokens)
  const setUser = useAuthStore((s) => s.setUser)
  const logout = useAuthStore((s) => s.logout)
  const [initializing, setInitializing] = useState(true)
  const [authenticated, setAuthenticated] = useState(false)
  const initialized = useRef(false)

  useEffect(() => {
    if (initialized.current) return
    initialized.current = true

    async function init() {
      try {
        if (!accessToken) {
          const res = await fetch('/api/auth/refresh', {
            method: 'POST',
            credentials: 'include',
          })
          if (!res.ok) {
            logout()
            router.push('/login')
            return
          }
          const { access_token } = await res.json()
          setTokens(access_token)
        }

        const meRes = await apiFetch('/api/auth/me')
        if (!meRes.ok) {
          logout()
          router.push('/login')
          return
        }

        const me = await meRes.json()
        setUser(mapUser(me))
        setAuthenticated(true)
      } catch {
        logout()
        router.push('/login')
      } finally {
        setInitializing(false)
      }
    }

    init()
  }, [accessToken, logout, router, setTokens, setUser])

  if (initializing) {
    return <PageLoading />
  }

  if (!authenticated) {
    return <PageLoading />
  }

  return <>{children}</>
}

