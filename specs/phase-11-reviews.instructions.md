---
description: "Phase 11 spec - User reviews: one verified review per user, admin approval, and public landing carousel."
applyTo: "backend/**, frontend/**, specs/**"
---

# Phase 11 - User Reviews

## Overview

FreeLingo adds a first-party review system so authenticated users can leave one verified rating for the product. Reviews are stored in PostgreSQL, moderated by admins, and approved positive reviews are displayed on the public landing page as social proof. The reusable review prompt is shown after successful learning moments: when the user manually stops a voice conversation session that has been live for at least five minutes, or when completing a lesson advances them out of the current curriculum unit. Users can also create or edit their review from Settings.

---

## Product rules

- Each user can create **one review total**.
- Users can edit their existing review from Settings; edits keep the same review row and reset `is_approved=false` so the changed review is moderated again.
- Users can delete their existing review from Settings after confirmation.
- If a user already has a review, the app must not ask for another one.
- `rating` is mandatory and must be an integer from `1` to `5`.
- `comment` is optional.
- The review stores a snapshot of the user's visible display name at creation time and refreshes it on user edits.
- The review stores the user's active learning language at creation time and refreshes it on user edits.
- Reviews are created with `is_approved=false` by default.
- Only admins can approve, unapprove, or delete reviews.
- The public landing page shows only reviews where `is_approved=true` and `rating >= 4`.
- Reviews without comments can still be shown on the landing page.
- Cancelling or closing the review prompt must not create anything in the backend.
- The frontend may store a local prompt cooldown/counter in `localStorage` to avoid asking too often after cancellation.
- The voice conversation page may ask for a review after a manually stopped voice session that has been connected for at least 5 minutes.
- The lesson completion page may ask for a review when completing the lesson moves the user into a different curriculum unit, or completes the plan.
- The backend remains the source of truth for duplicate prevention; the prompt checks `GET /api/reviews/me` and does not render for users who already have a review.

---

## Out of scope

- Tracking where the review prompt was shown.
- Tracking which event triggered the review prompt.
- Multiple reviews per user.
- Admin editing of review text.
- Public display of unapproved reviews.
- Public display of ratings below 4 stars.
- Additional dashboard or progress prompt triggers beyond the voice conversation and unit-completion triggers.

---

## Database model

Status: implemented in `backend/app/models/review.py` and migration `backend/alembic/versions/0042_reviews.py`.

### `reviews`

| Column            | Type        | Constraints                                | Notes                                      |
| ----------------- | ----------- | ------------------------------------------ | ------------------------------------------ |
| id                | integer     | PK, autoincrement                          |                                            |
| user_id           | integer     | NOT NULL, FK -> users(CASCADE), UNIQUE     | Enforces one review per user               |
| user_display_name | string(150) | NOT NULL                                   | Snapshot at creation time                  |
| target_language   | string(10)  | NOT NULL, index                            | Active learning language at creation time  |
| rating            | integer     | NOT NULL, check `rating BETWEEN 1 AND 5`   | 1-5 stars                                  |
| comment           | text        | nullable                                   | Optional user comment                      |
| is_approved       | boolean     | NOT NULL, default `false`, index           | Admin moderation gate                      |
| created_at        | datetime    | NOT NULL, index                            | UTC, tz-naive                              |
| updated_at        | datetime    | NOT NULL                                   | Updated on approval state changes          |

### Constraints and indexes

- `uq_reviews_user_id` - `UNIQUE(user_id)`, one review per user.
- `ck_reviews_rating_range` - `CHECK(rating >= 1 AND rating <= 5)`, database-level rating guard.
- Index `target_language` for admin filtering and public display grouping.
- Index `is_approved` for landing/public review queries.
- Index `created_at` for newest-first admin lists.

### Alembic migration

`backend/alembic/versions/0042_reviews.py` - revision `0042_reviews`, down_revision `0041_backfill_learning_goals`.

Creates `reviews` with all constraints and indexes. Fully reversible via `downgrade()`.

### Snapshot rules

- `user_display_name` is copied when the review is created and refreshed when the user edits their review.
- If the user changes their profile later without editing the review, the existing review display name does not change.
- The active learning language is copied from the current active study language/user-language state when the review is created and refreshed when the user edits their review.

---

## Backend API

Status: implemented in `backend/app/routers/reviews.py` and registered in `backend/app/main.py`.

### User endpoints - `/api/reviews`

- **GET `/me`** - Rate limit: 60/min. Auth: `get_current_user`. Returns the authenticated user's review if it exists, otherwise a no-review response.
- **POST `/`** - Rate limit: 5/hour. Auth: `get_current_user`. Creates the authenticated user's review. Body requires `rating`; `comment` is optional. Returns HTTP 201. Returns HTTP 409 if the user already has a review.
- **PATCH `/me`** - Rate limit: 10/hour. Auth: `get_current_user`. Updates the authenticated user's existing review. Body requires `rating`; `comment` is optional. Refreshes snapshots and resets `is_approved=false`. Returns HTTP 404 if no review exists.
- **DELETE `/me`** - Rate limit: 10/hour. Auth: `get_current_user`. Deletes the authenticated user's existing review. Returns HTTP 204, or HTTP 404 if no review exists.

### Public endpoint - `/api/reviews/public`

- **GET `/`** - Rate limit: 60/min. Public endpoint for the landing page. Returns approved reviews with `rating >= 4`, ordered newest-first. Query param: `limit` (default 20, max 100).

### Admin endpoints - `/api/admin/reviews`

- **GET `/`** - Rate limit: 60/min. Auth: `require_admin`. Lists all reviews with pagination and optional filters: `is_approved`, `rating`, `target_language`, `order`, `skip`, `limit`.
- **PATCH `/{review_id}`** - Rate limit: 60/min. Auth: `require_admin`. Updates `is_approved` to approve or unapprove a review.
- **DELETE `/{review_id}`** - Rate limit: 60/min. Auth: `require_admin`. Permanently deletes a review.

### Rate limits

- `GET /api/reviews/me` - 60/min.
- `POST /api/reviews` - 5/hour.
- `PATCH /api/reviews/me` - 10/hour.
- `DELETE /api/reviews/me` - 10/hour.
- `GET /api/reviews/public` - 60/min.
- `GET /api/admin/reviews` - 60/min.
- `PATCH /api/admin/reviews/{review_id}` - 60/min.
- `DELETE /api/admin/reviews/{review_id}` - 60/min.

---

## Backend schemas

Status: implemented in `backend/app/schemas/review.py`.

- `ReviewCreate` - `rating: int` constrained to 1-5; `comment: str | None` with a practical max length.
- `ReviewUpdate` - same fields and validation as `ReviewCreate`, used for current-user review edits.
- `ReviewMeResponse` - existing review or `review: null` plus `has_review: bool`.
- `ReviewPublicOut` - `id`, `user_display_name`, `target_language`, `rating`, `comment`, `created_at`.
- `ReviewAdminOut` - public fields plus `user_id`, `is_approved`, `updated_at`.
- `ReviewApprovalUpdate` - `is_approved: bool`.
- `PaginatedReviewsResponse` - `{items, total, skip, limit}` for admin lists.

---

## Backend service behaviour

Status: implemented in `backend/app/services/review_service.py`.

- Creating a review must be atomic enough to handle duplicate submissions safely.
- Duplicate creation attempts return HTTP 409 rather than overwriting the existing review.
- The service must derive `user_display_name` server-side from the authenticated user.
- The service must derive `target_language` server-side from the current active learning language.
- Editing a review must update `rating`, normalized `comment`, `user_display_name`, `target_language`, and `updated_at`, and must reset `is_approved=false`.
- Deleting a review must be scoped to the authenticated user's `user_id`.
- Public listing must never return unapproved reviews.
- Public listing must never return reviews with `rating < 4`.
- Deleting a user cascades and removes their review.

---

## Frontend behaviour

Status: implemented.

### API client

Add review API helpers for:

- Fetching the current user's review state.
- Creating a review.
- Updating the current user's existing review.
- Deleting the current user's existing review.
- Fetching public landing reviews.
- Admin listing reviews.
- Admin approving/unapproving reviews.
- Admin deleting reviews.

Implemented in `frontend/src/lib/reviews.ts` with shared types in `frontend/src/types/api.ts`.

### Review form and prompt components

The form is reusable and shared by the automatic modal prompt and the Settings review section. The prompt can be mounted by any future product flow.

Implemented in `frontend/src/components/reviews/ReviewPrompt.tsx`.

Required UI:

- 1-5 star selector.
- Optional comment textarea.
- Submit button.
- Cancel/close action.
- Loading and error states.

Required behaviour:

- It must not submit without a rating.
- It must allow rating-only submissions.
- It must allow rating plus comment submissions.
- It must check whether the user already has a review before showing or before submitting.
- If that existing-review status check fails, the prompt must show an error-only state and must not allow submission.
- Cancel/close must not call the backend create endpoint.
- Cancel/close may update a `localStorage` cooldown/counter so the app does not ask too often.

### Settings review section

Implemented in `frontend/src/components/settings/ReviewSection.tsx` and mounted below `BillingSection` on `frontend/src/app/(app)/settings/page.tsx`.

Required behaviour:

- Fetch `GET /api/reviews/me` on load.
- Render the shared review form empty when no review exists.
- Render the shared review form prefilled when the user already has a review.
- Submit new reviews with `POST /api/reviews`.
- Submit edits with `PATCH /api/reviews/me`.
- Delete existing reviews with `DELETE /api/reviews/me` after a confirmation dialog.
- Show a pending-approval hint for reviews where `is_approved=false`.
- Show a short saved/deleted confirmation after successful create/update/delete.

### Prompt cooldown

The cooldown is client-side only.

Recommended localStorage data:

- Count of dismissed prompts.
- Last dismissed timestamp.

The backend remains the source of truth for whether a review exists.

Implemented storage key: `freelingo:reviewPromptDismissed`.

Implemented voice-conversation trigger:

- `frontend/src/components/conversation/ConversationMode.tsx` records a local session start timestamp when the voice WebSocket opens.
- When the user manually presses Stop, the prompt is opened only if that live connected duration is at least 5 minutes.
- Backend quota/session duration accounting remains separate and authoritative for usage limits; the local timestamp is only used to decide whether to show the review prompt immediately after Stop.
- The trigger uses `frontend/src/lib/review-prompt-triggers.ts` to enforce the 5-minute threshold, a 14-day local dismissal cooldown, and a maximum of 3 local dismissals.

Implemented unit-completion trigger:

- `frontend/src/app/(app)/lesson/[id]/page.tsx` records the completed lesson's `content.unit_id` before marking the lesson complete.
- After completion, it calls `GET /api/study-plan/today` and compares the next available lesson `unit_id` with the completed lesson's unit.
- The prompt opens when the next unit differs, or when the plan is complete (`progress_day >= total_days`).
- If the next lesson cannot be generated and the plan is not complete, the prompt is not shown; this avoids asking for a review on transient lesson-generation failures.
- The trigger uses the shared local dismissal cooldown and maximum dismissal count from `frontend/src/lib/review-prompt-triggers.ts`.

---

## Landing page

Add a public reviews/testimonials section powered by `GET /api/reviews/public`.

Implemented in `frontend/src/components/reviews/LandingReviewsCarousel.tsx` and mounted on `frontend/src/app/page.tsx` between the features section and pricing section.

When public reviews are available, `frontend/src/components/ui/landing-nav.tsx` shows a Reviews link in the landing navigation between Features and Pricing. The link targets the reviews carousel section and is included in both desktop and mobile menus. If no reviews are returned, the nav link is hidden with the section.

Display rules:

- Show approved reviews with `rating >= 4`.
- Show user display name.
- Show active learning language in a user-friendly label.
- Show star rating.
- Show comment when present.
- For reviews without comment, show a short neutral fallback such as "Verified FreeLingo rating".
- Review cards use a consistent card height and clamp comments to 6 lines with an ellipsis so long comments do not break the carousel layout.
- Handle an empty list without rendering a broken or sparse section.

Recommended placement:

- After the main benefits/value section.
- Before the final conversion CTA.

UX requirements:

- Carousel/slider presentation.
- Automatic horizontal scrolling or auto-advance.
- Manual scrolling must still work.
- Responsive layout for desktop and mobile.
- Accessible star labels, not visual-only rating information.

---

## Admin UI

Add a new admin reviews section.

Implemented at `frontend/src/app/(app)/admin/reviews/page.tsx`, with navigation entry in `frontend/src/components/admin/AdminNav.tsx`.

The admin overview (`/admin`) also surfaces reviews waiting for approval via the `reviews_pending` field from `GET /api/admin/stats` and includes a quick-link card to the review moderation section.

Required fields:

- User display name.
- Learning language.
- Rating.
- Comment.
- Approval state.
- Creation date.

Required actions:

- Approve.
- Unapprove.
- Delete with confirmation.
- After deleting a review, reload the effective active page so later reviews fill the list and page bounds stay valid.

Recommended filters:

- All.
- Pending.
- Approved.
- Rating.

Admin should not edit review content. If content is not acceptable, the review should remain unapproved or be deleted.

---

## Admin email notifications

When a user creates a new product review with `POST /api/reviews`, an email is sent to `CONTACT_EMAIL` (if `EMAIL_ENABLED=true` and `CONTACT_EMAIL` is configured).

- **Triggered by:** `POST /api/reviews` only. Editing an existing review with `PATCH /api/reviews/me` does not send a notification.
- **Language:** native language of the first admin user by ascending `id`, with English fallback for unsupported locales.
- **Subject:** localized equivalent of `[New Review] <rating>/5 — <display name>`.
- **Template:** `backend/app/templates/email/review_submitted.html` — shows reviewer display name, rating, learning language, optional comment, and a link to the admin review moderation queue at `APP_BASE_URL/admin/reviews`.
- **Implementation:** `email_service.send_review_notification()`. Called via `asyncio.create_task()` after the review is committed to avoid blocking the HTTP response. Errors are logged but never re-raised — the review is already persisted.
- **Config:** reuses existing `EMAIL_ENABLED` and `CONTACT_EMAIL` settings; no new env vars required.

---

## Backend tests

- Create a valid review.
- Reject missing rating.
- Reject `rating < 1`.
- Reject `rating > 5`.
- Allow missing or empty comment.
- Reject a second review for the same user with HTTP 409.
- Creating a review sends one admin email notification in the first admin's native language.
- Updating an existing review does not send a review-created admin email notification.
- `GET /api/reviews/me` returns no-review state when absent.
- `GET /api/reviews/me` returns the user's review when present.
- Public endpoint excludes unapproved reviews.
- Public endpoint excludes approved reviews with `rating < 4`.
- Public endpoint includes approved reviews with `rating >= 4`.
- Admin can list reviews.
- Admin can approve a review.
- Admin can unapprove a review.
- Admin can delete a review.
- Non-admin users cannot access admin review endpoints.

---

## Frontend tests

Status: implemented.

- Review prompt does not submit without rating.
- Review prompt submits rating-only reviews.
- Review prompt submits rating plus comment reviews.
- Cancel/close does not call the create-review API.
- Local prompt cooldown/counter is updated on cancel if implemented in shared logic.
- Voice conversation review trigger requires at least 5 minutes of connected session time.
- Voice conversation review trigger respects dismissal cooldown and maximum dismissal count.
- Unit-completion review trigger opens only when a unit was completed.
- Unit-completion review trigger respects dismissal cooldown and maximum dismissal count.
- Landing reviews section renders reviews with comments.
- Landing reviews section renders reviews without comments.
- Landing reviews section handles an empty list.
- Admin reviews page renders review rows/cards.
- Admin reviews page calls approve/unapprove actions.
- Admin reviews page calls delete only after confirmation.

Implemented test files:

- `frontend/tests/lib/reviews.test.ts`
- `frontend/tests/lib/review-prompt-triggers.test.ts`
- `frontend/tests/components/ReviewPrompt.test.tsx`
- `frontend/tests/components/LandingReviewsCarousel.test.tsx`
- `frontend/tests/app/admin-reviews.test.tsx`

---

## Implementation phases

1. **Spec and planning** - this document plus affected architecture/API/database/frontend documentation updates.
2. **Backend model and migration** - `Review` ORM model, Alembic migration, constraints, relationships. Status: complete.
3. **Backend schemas and service** - validation, one-review guard, public/admin query helpers. Status: complete.
4. **Backend endpoints** - user, public, and admin routes with rate limits. Status: complete.
5. **Backend tests** - coverage for creation, constraints, moderation, public filtering, permissions. Status: complete.
6. **Frontend API client** - types and helper functions. Status: complete.
7. **Reusable prompt component** - star rating, optional comment, cancellation cooldown. Status: complete.
8. **Landing section** - approved positive reviews carousel. Status: complete.
9. **Admin section** - list, filters, approve/unapprove, delete. Status: complete.
10. **Frontend tests** - prompt, landing, admin interactions. Status: complete.
11. **Verification** - compile/typecheck and targeted test runs. Status: complete for current implementation.
12. **Documentation finalization** - update specs, changelog, and version docs according to the release scope.

---

## Documentation impact checklist

When Phase 11 is implemented, review and update these docs as needed:

- `specs/database-models.instructions.md` - new `reviews` model.
- `specs/api-endpoints.instructions.md` - new user/public/admin endpoints.
- `specs/architecture-backend.instructions.md` - new model, schema, router/service counts and file list.
- `specs/architecture-frontend.instructions.md` - new review components, landing section, admin page, API helpers.
- `specs/rate-limiting.instructions.md` - review creation/public/admin limits.
- `specs/services.instructions.md` - review service if implemented as a dedicated service.
- `README.md` - user-facing feature summary if included in release notes.
- `AGENTS.md` - project state and authoritative spec list.
- `CHANGELOG.md` - user-visible feature entry.
- `specs/version.md` - version bump if included in a release.
