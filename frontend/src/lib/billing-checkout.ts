export type BillingInterval = 'monthly' | 'yearly'

const LAST_CHECKOUT_PLAN_KEY = 'fl_last_checkout_plan'

export function saveLastCheckoutPlan(plan: BillingInterval) {
  try {
    localStorage.setItem(LAST_CHECKOUT_PLAN_KEY, plan)
  } catch {
    // Checkout must continue even if storage is unavailable.
  }
}

export function getLastCheckoutPlan(): BillingInterval | null {
  try {
    const plan = localStorage.getItem(LAST_CHECKOUT_PLAN_KEY)
    return plan === 'monthly' || plan === 'yearly' ? plan : null
  } catch {
    return null
  }
}
