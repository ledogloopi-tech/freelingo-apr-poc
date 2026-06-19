'use client'

import { useEffect, useState } from 'react'
import { useTranslations } from 'next-intl'
import { Loader2, Star, X } from 'lucide-react'
import { createReview, fetchMyReview } from '@/lib/reviews'
import type { ReviewAdmin } from '@/types/api'

const DISMISS_KEY = 'freelingo:reviewPromptDismissed'

export function getReviewPromptDismissal(): {
  count: number
  lastDismissedAt: number
} {
  if (typeof window === 'undefined') return { count: 0, lastDismissedAt: 0 }
  try {
    const raw = window.localStorage.getItem(DISMISS_KEY)
    if (!raw) return { count: 0, lastDismissedAt: 0 }
    const parsed = JSON.parse(raw) as {
      count?: number
      lastDismissedAt?: number
    }
    return {
      count: Number(parsed.count) || 0,
      lastDismissedAt: Number(parsed.lastDismissedAt) || 0,
    }
  } catch {
    return { count: 0, lastDismissedAt: 0 }
  }
}

export function recordReviewPromptDismissal(): void {
  if (typeof window === 'undefined') return
  const current = getReviewPromptDismissal()
  window.localStorage.setItem(
    DISMISS_KEY,
    JSON.stringify({ count: current.count + 1, lastDismissedAt: Date.now() })
  )
}

interface ReviewPromptProps {
  open: boolean
  onClose: () => void
  onSubmitted?: (review: ReviewAdmin) => void
}

export function ReviewPrompt({
  open,
  onClose,
  onSubmitted,
}: ReviewPromptProps) {
  const t = useTranslations('reviewPrompt')
  const [checking, setChecking] = useState(false)
  const [hasReview, setHasReview] = useState(false)
  const [rating, setRating] = useState(0)
  const [comment, setComment] = useState('')
  const [submitting, setSubmitting] = useState(false)
  const [error, setError] = useState('')
  const [statusCheckFailed, setStatusCheckFailed] = useState(false)

  useEffect(() => {
    if (!open) return
    let cancelled = false
    setChecking(true)
    setError('')
    setStatusCheckFailed(false)
    fetchMyReview()
      .then((data) => {
        if (cancelled) return
        setHasReview(data.has_review)
      })
      .catch(() => {
        if (cancelled) return
        setStatusCheckFailed(true)
        setError(t('statusError'))
      })
      .finally(() => {
        if (!cancelled) setChecking(false)
      })
    return () => {
      cancelled = true
    }
  }, [open, t])

  if (!open || hasReview) return null

  function handleCancel() {
    recordReviewPromptDismissal()
    onClose()
  }

  async function handleSubmit() {
    if (statusCheckFailed) return
    if (!rating) {
      setError(t('ratingRequiredError'))
      return
    }
    setSubmitting(true)
    setError('')
    try {
      const review = await createReview({
        rating,
        comment: comment.trim() || undefined,
      })
      onSubmitted?.(review)
      onClose()
    } catch {
      setError(t('saveError'))
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <div className="fixed inset-0 z-[180] flex items-center justify-center bg-black/70 p-4 backdrop-blur-sm">
      <div className="border-fl-border bg-fl-surface w-full max-w-md border shadow-2xl">
        <div className="border-fl-border flex items-center justify-between border-b px-5 py-4">
          <div>
            <p className="text-fl-label text-fl-muted-2 font-mono tracking-widest uppercase">
              {t('eyebrow')}
            </p>
            <h2 className="text-fl-fg mt-1 font-sans text-lg font-semibold tracking-tight">
              {t('title')}
            </h2>
          </div>
          <button
            type="button"
            onClick={handleCancel}
            className="text-fl-muted-2 hover:text-fl-fg p-2 transition-colors"
            aria-label={t('closeLabel')}
          >
            <X className="size-4" />
          </button>
        </div>

        <div className="space-y-5 px-5 py-5">
          {checking ? (
            <div className="text-fl-muted-2 flex items-center gap-2 font-mono text-xs">
              <Loader2 className="size-4 animate-spin" /> {t('checking')}
            </div>
          ) : statusCheckFailed ? (
            <p className="text-fl-error-fg font-mono text-xs">{error}</p>
          ) : (
            <>
              <div>
                <p className="text-fl-label text-fl-muted-2 mb-3 font-mono tracking-widest uppercase">
                  {t('ratingLabel')}
                </p>
                <div
                  className="flex gap-2"
                  role="radiogroup"
                  aria-label={t('ratingGroupLabel')}
                >
                  {[1, 2, 3, 4, 5].map((value) => (
                    <button
                      key={value}
                      type="button"
                      role="radio"
                      aria-checked={rating === value}
                      aria-label={`${value} ${t(value === 1 ? 'star' : 'stars')}`}
                      onClick={() => setRating(value)}
                      className={`border px-3 py-2 transition-colors ${
                        value <= rating
                          ? 'border-yellow-400 text-yellow-400'
                          : 'border-fl-border text-fl-muted-3 hover:text-fl-fg'
                      }`}
                    >
                      <Star className="size-5 fill-current" />
                    </button>
                  ))}
                </div>
              </div>

              <div>
                <label
                  htmlFor="review-comment"
                  className="text-fl-label text-fl-muted-2 mb-2 block font-mono tracking-widest uppercase"
                >
                  {t('commentLabel')}
                </label>
                <textarea
                  id="review-comment"
                  value={comment}
                  onChange={(event) => setComment(event.target.value)}
                  maxLength={2000}
                  rows={4}
                  className="border-fl-border bg-fl-bg text-fl-fg placeholder:text-fl-muted-4 focus:border-fl-accent w-full resize-none border px-3 py-2 font-mono text-sm outline-none"
                  placeholder={t('commentPlaceholder')}
                />
              </div>

              {error && (
                <p className="text-fl-error-fg font-mono text-xs">{error}</p>
              )}
            </>
          )}
        </div>

        <div className="flex gap-2 px-5 pb-5">
          <button
            type="button"
            onClick={handleCancel}
            className="border-fl-border text-fl-label text-fl-muted-2 hover:text-fl-fg flex-1 border py-3 font-mono font-bold tracking-widest uppercase transition-colors"
          >
            {t('cancel')}
          </button>
          <button
            type="button"
            onClick={handleSubmit}
            disabled={checking || submitting || statusCheckFailed}
            className="bg-fl-accent text-fl-accent-fg text-fl-label hover:bg-fl-accent/90 flex flex-1 items-center justify-center gap-2 py-3 font-mono font-bold tracking-widest uppercase transition-colors disabled:opacity-60"
          >
            {submitting && <Loader2 className="size-3.5 animate-spin" />}
            {t('submit')}
          </button>
        </div>
      </div>
    </div>
  )
}
