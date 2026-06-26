'use client'

import { useEffect, useState } from 'react'
import Image from 'next/image'
import { useAuthStore } from '@/store/auth'

interface Props {
  avatar: string
  alt?: string
  width: number
  height: number
  className?: string
}

export function AuthAvatarImage({
  avatar,
  alt = '',
  width,
  height,
  className,
}: Props) {
  const accessToken = useAuthStore((state) => state.accessToken)
  const [src, setSrc] = useState<string | null>(null)

  useEffect(() => {
    let active = true
    let objectUrl: string | null = null

    if (avatar.startsWith('data:image/')) {
      setSrc(avatar)
      return
    }

    setSrc(null)

    async function loadAvatar() {
      try {
        const headers: HeadersInit = accessToken
          ? { Authorization: `Bearer ${accessToken}` }
          : {}
        const res = await fetch('/api/auth/me/avatar-file', {
          headers,
          credentials: 'include',
        })
        if (!res.ok) return
        const blob = await res.blob()
        objectUrl = URL.createObjectURL(blob)
        if (active) {
          setSrc(objectUrl)
        } else {
          URL.revokeObjectURL(objectUrl)
        }
      } catch {
        if (objectUrl) URL.revokeObjectURL(objectUrl)
      }
    }

    void loadAvatar()

    return () => {
      active = false
      if (objectUrl) URL.revokeObjectURL(objectUrl)
    }
  }, [accessToken, avatar])

  if (!src) return null

  return (
    <Image
      src={src}
      alt={alt}
      width={width}
      height={height}
      className={className}
      unoptimized
    />
  )
}
