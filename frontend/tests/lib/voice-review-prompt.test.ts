import { describe, expect, it } from 'vitest'
import {
  VOICE_REVIEW_PROMPT_DISMISS_COOLDOWN_MS,
  VOICE_REVIEW_PROMPT_MAX_DISMISSALS,
  VOICE_REVIEW_PROMPT_MIN_SESSION_MS,
  shouldShowVoiceReviewPrompt,
} from '@/lib/voice-review-prompt'

describe('voice review prompt trigger', () => {
  it('does not show before the minimum session duration', () => {
    expect(
      shouldShowVoiceReviewPrompt(
        { count: 0, lastDismissedAt: 0 },
        VOICE_REVIEW_PROMPT_MIN_SESSION_MS - 1
      )
    ).toBe(false)
  })

  it('shows after a long enough session when there is no cooldown', () => {
    expect(
      shouldShowVoiceReviewPrompt(
        { count: 0, lastDismissedAt: 0 },
        VOICE_REVIEW_PROMPT_MIN_SESSION_MS
      )
    ).toBe(true)
  })

  it('does not show during dismissal cooldown', () => {
    const now = 1_000_000_000
    expect(
      shouldShowVoiceReviewPrompt(
        { count: 1, lastDismissedAt: now - 1_000 },
        VOICE_REVIEW_PROMPT_MIN_SESSION_MS,
        now
      )
    ).toBe(false)
  })

  it('shows after dismissal cooldown expires', () => {
    const now = 1_000_000_000
    expect(
      shouldShowVoiceReviewPrompt(
        {
          count: 1,
          lastDismissedAt: now - VOICE_REVIEW_PROMPT_DISMISS_COOLDOWN_MS,
        },
        VOICE_REVIEW_PROMPT_MIN_SESSION_MS,
        now
      )
    ).toBe(true)
  })

  it('does not show after the maximum dismissal count', () => {
    expect(
      shouldShowVoiceReviewPrompt(
        { count: VOICE_REVIEW_PROMPT_MAX_DISMISSALS, lastDismissedAt: 0 },
        VOICE_REVIEW_PROMPT_MIN_SESSION_MS
      )
    ).toBe(false)
  })
})
