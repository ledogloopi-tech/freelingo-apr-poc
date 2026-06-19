---
description: "Phase 11 spec - User reviews: one verified review per user, admin approval, and public landing carousel."
applyTo: "backend/**, frontend/**, specs/**"
---

# Phase 11 - User Reviews

## Overview

FreeLingo adds a first-party review system so authenticated users can leave one verified rating for the product. Reviews are stored in PostgreSQL, moderated by admins, and approved positive reviews are displayed on the public landing page as social proof.

This phase defines the feature contract only. The exact product moments where the review prompt appears are intentionally out of scope for this spec and will be decided later.

---

## Product rules

- Each user can create **one review total**.
- If a user already has a review, the app must not ask for another one.
- `rating` is mandatory and must be an integer from `1` to `5`.
- `comment` is optional.
- The review stores a snapshot of the user's visible display name at creation time.
- The review stores the user's active learning language at creation time.
- Reviews are created with `is_approved=false` by default.
- Only admins can approve, unapprove, or delete reviews.
- The public landing page shows only reviews where `is_approved=true` and `rating >= 4`.
- Reviews without comments can still be shown on the landing page.
- Cancelling or closing the review prompt must not create anything in the backend.
- The frontend may store a local prompt cooldown/counter in `localStorage` to avoid asking too often after cancellation.

---

## Out of scope

- Tracking where the review prompt was shown.
- Tracking which event triggered the review prompt.
- Multiple reviews per user.
- Review editing by users.
- Admin editing of review text.
- Public display of unapproved reviews.
- Public display of ratings below 4 stars.
- Defining the exact lesson, conversation, dashboard, or progress moments where the prompt appears.

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

- `user_display_name` is copied when the review is created.
- If the user changes their profile later, the existing review display name does not change.
- The active learning language is copied from the current active study language/user-language state when the review is created.

---

## Backend API

Status: implemented in `backend/app/routers/reviews.py` and registered in `backend/app/main.py`.

### User endpoints - `/api/reviews`

- **GET `/me`** - Rate limit: 60/min. Auth: `get_current_user`. Returns the authenticated user's review if it exists, otherwise a no-review response.
- **POST `/`** - Rate limit: 5/hour. Auth: `get_current_user`. Creates the authenticated user's review. Body requires `rating`; `comment` is optional. Returns HTTP 201. Returns HTTP 409 if the user already has a review.

### Public endpoint - `/api/reviews/public`

- **GET `/`** - Rate limit: 60/min. Public endpoint for the landing page. Returns approved reviews with `rating >= 4`, ordered newest-first. Query param: `limit` (default 20, max 100).

### Admin endpoints - `/api/admin/reviews`

- **GET `/`** - Rate limit: 60/min. Auth: `require_admin`. Lists all reviews with pagination and optional filters: `is_approved`, `rating`, `target_language`, `order`, `skip`, `limit`.
- **PATCH `/{review_id}`** - Rate limit: 60/min. Auth: `require_admin`. Updates `is_approved` to approve or unapprove a review.
- **DELETE `/{review_id}`** - Rate limit: 60/min. Auth: `require_admin`. Permanently deletes a review.

### Rate limits

- `GET /api/reviews/me` - 60/min.
- `POST /api/reviews` - 5/hour.
- `GET /api/reviews/public` - 60/min.
- `GET /api/admin/reviews` - 60/min.
- `PATCH /api/admin/reviews/{review_id}` - 60/min.
- `DELETE /api/admin/reviews/{review_id}` - 60/min.

---

## Backend schemas

Status: implemented in `backend/app/schemas/review.py`.

- `ReviewCreate` - `rating: int` constrained to 1-5; `comment: str | None` with a practical max length.
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
- Public listing must never return unapproved reviews.
- Public listing must never return reviews with `rating < 4`.
- Deleting a user cascades and removes their review.

---

## Frontend behaviour

### API client

Add review API helpers for:

- Fetching the current user's review state.
- Creating a review.
- Fetching public landing reviews.
- Admin listing reviews.
- Admin approving/unapproving reviews.
- Admin deleting reviews.

### Review prompt component

The prompt is reusable and can be mounted by any future product flow.

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
- Cancel/close must not call the backend create endpoint.
- Cancel/close may update a `localStorage` cooldown/counter so the app does not ask too often.

### Prompt cooldown

The cooldown is client-side only.

Recommended localStorage data:

- Count of dismissed prompts.
- Last dismissed timestamp.

The backend remains the source of truth for whether a review exists.

---

## Landing page

Add a public reviews/testimonials section powered by `GET /api/reviews/public`.

Display rules:

- Show approved reviews with `rating >= 4`.
- Show user display name.
- Show active learning language in a user-friendly label.
- Show star rating.
- Show comment when present.
- For reviews without comment, show a short neutral fallback such as "Verified FreeLingo rating".
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

Recommended filters:

- All.
- Pending.
- Approved.
- Rating.

Admin should not edit review content. If content is not acceptable, the review should remain unapproved or be deleted.

---

## Backend tests

- Create a valid review.
- Reject missing rating.
- Reject `rating < 1`.
- Reject `rating > 5`.
- Allow missing or empty comment.
- Reject a second review for the same user with HTTP 409.
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

- Review prompt does not submit without rating.
- Review prompt submits rating-only reviews.
- Review prompt submits rating plus comment reviews.
- Cancel/close does not call the create-review API.
- Local prompt cooldown/counter is updated on cancel if implemented in shared logic.
- Landing reviews section renders reviews with comments.
- Landing reviews section renders reviews without comments.
- Landing reviews section handles an empty list.
- Admin reviews page renders review rows/cards.
- Admin reviews page calls approve/unapprove actions.
- Admin reviews page calls delete only after confirmation.

---

## Implementation phases

1. **Spec and planning** - this document plus affected architecture/API/database/frontend documentation updates.
2. **Backend model and migration** - `Review` ORM model, Alembic migration, constraints, relationships. Status: complete.
3. **Backend schemas and service** - validation, one-review guard, public/admin query helpers. Status: complete.
4. **Backend endpoints** - user, public, and admin routes with rate limits. Status: complete.
5. **Backend tests** - coverage for creation, constraints, moderation, public filtering, permissions. Status: complete.
6. **Frontend API client** - types and helper functions.
7. **Reusable prompt component** - star rating, optional comment, cancellation cooldown.
8. **Landing section** - approved positive reviews carousel.
9. **Admin section** - list, filters, approve/unapprove, delete.
10. **Frontend tests** - prompt, landing, admin interactions.
11. **Verification** - compile/typecheck and targeted test runs.
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
