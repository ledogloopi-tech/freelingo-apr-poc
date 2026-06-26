'use client'

import { useEffect, useState } from 'react'
import Image from 'next/image'
import { loadAvatar, subscribeAvatar } from '@/lib/avatar-cache'
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
    const unsubscribe = subscribeAvatar(setSrc)
    void loadAvatar(avatar, accessToken)
    return unsubscribe
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
