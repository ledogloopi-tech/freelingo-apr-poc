'use client'

import { useEffect, useState } from 'react'
import { useTranslations } from 'next-intl'
import { Loader2 } from 'lucide-react'
import { ReviewForm } from '@/components/reviews/ReviewPrompt'
import { createReview, fetchMyReview, updateMyReview } from '@/lib/reviews'
import type { ReviewAdmin } from '@/types/api'

export function ReviewSection() {
  const t = useTranslations('settings')
  const tReview = useTranslations('reviewPrompt')
  const [review, setReview] = useState<ReviewAdmin | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [saved, setSaved] = useState(false)

  useEffect(() => {
    let cancelled = false
    setLoading(true)
    setError('')
    fetchMyReview()
      .then((data) => {
        if (!cancelled) setReview(data.review)
      })
      .catch(() => {
        if (!cancelled) setError(tReview('statusError'))
      })
      .finally(() => {
        if (!cancelled) setLoading(false)
      })
    return () => {
      cancelled = true
    }
  }, [tReview])

  return (
    <div className="border-fl-border bg-fl-surface mt-4 border p-6">
      <div className="border-fl-border mb-4 flex items-center gap-2 border-b pb-4">
        <span className="text-fl-label text-fl-muted-2">●</span>
        <span className="text-fl-label text-fl-muted-2 font-mono tracking-widest uppercase">
          {t('sectionReview')}
        </span>
      </div>

      <p className="text-fl-muted-2 mb-1 font-mono text-sm leading-relaxed">
        {t('reviewDescription')}
      </p>
      {review?.is_approved === false && (
        <p className="text-fl-hint text-fl-muted-4 mb-4 font-mono tracking-widest uppercase">
          {t('reviewPending')}
        </p>
      )}

      {loading ? (
        <div className="text-fl-muted-2 flex items-center gap-2 py-5 font-mono text-xs">
          <Loader2 className="size-4 animate-spin" /> {tReview('checking')}
        </div>
      ) : error ? (
        <p className="text-fl-error-fg py-5 font-mono text-xs">{error}</p>
      ) : (
        <div className="-mx-5">
          <ReviewForm
            initialReview={review}
            submitLabel={review ? t('reviewUpdate') : tReview('submit')}
            onSubmit={async (data) => {
              const savedReview = review
                ? await updateMyReview(data)
                : await createReview(data)
              setReview(savedReview)
              setSaved(true)
              window.setTimeout(() => setSaved(false), 2500)
              return savedReview
            }}
          />
          {saved && (
            <p className="text-fl-accent px-5 pb-5 font-mono text-xs">
              {t('reviewSaved')}
            </p>
          )}
        </div>
      )}
    </div>
  )
}
