export const VOICE_REVIEW_PROMPT_MIN_SESSION_MS = 5 * 60 * 1000
export const VOICE_REVIEW_PROMPT_DISMISS_COOLDOWN_MS = 14 * 24 * 60 * 60 * 1000
export const VOICE_REVIEW_PROMPT_MAX_DISMISSALS = 3

export function shouldShowVoiceReviewPrompt(
  dismissal: { count: number; lastDismissedAt: number },
  sessionDurationMs: number,
  now = Date.now()
): boolean {
  if (sessionDurationMs < VOICE_REVIEW_PROMPT_MIN_SESSION_MS) return false
  if (dismissal.count >= VOICE_REVIEW_PROMPT_MAX_DISMISSALS) return false
  if (
    dismissal.lastDismissedAt > 0 &&
    now - dismissal.lastDismissedAt < VOICE_REVIEW_PROMPT_DISMISS_COOLDOWN_MS
  ) {
    return false
  }
  return true
}
