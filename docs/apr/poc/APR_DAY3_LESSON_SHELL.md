# APR Day 3 Lesson Shell

## 1. Goal

Build a reusable Academia Português Reconectado (APR) lesson-player shell and a versioned, typed lesson-content contract inside the isolated APR boundary.

This Day 3 implementation proves structure and interaction only. It does not author final Lesson 1 curriculum.

## 2. Branch

`codex/apr-day3-lesson-shell`

## 3. Content-contract structure

The backend defines an APR lesson manifest with:

- `lesson_id`
- `module_id`
- `version`
- `title`
- `internal_title`
- `content_status`
- `authorized_for_pilot`
- `authorized_for_public_release`
- `estimated_minutes`
- `current_step_count`
- `steps`

Each step includes:

- `step_id`
- `step_type`
- `title`
- `body`
- `required`

Single-choice steps also include options with fixed option feedback. Reflection steps include a prompt, optional placeholder, and maximum character count.

## 4. Backend endpoint

`GET /api/apr/modules/primeira-conexao/lessons/enter-the-connection`

The endpoint uses the existing APR router namespace and existing authenticated-user dependency. It returns one fixed typed manifest when `APR_POC_ENABLED=true` and returns 404 when APR is disabled.

The endpoint does not require CEFR placement, a study plan, progress state, subscriptions, billing, or any database write.

## 5. Frontend route

Browser route:

`/apr/primeira-conexao/lessons/enter-the-connection`

Page file:

`frontend/src/app/(apr)/apr/primeira-conexao/lessons/enter-the-connection/page.tsx`

The page is under the isolated `(apr)` route group and uses the auth-only APR layout from Day 2 rather than the inherited FreeLingo `(app)` layout.

## 6. Supported step types

Day 3 supports only:

- `orientation`
- `information`
- `single_choice`
- `reflection`

This is intentionally not a universal course-authoring engine.

## 7. Session-state behavior

The lesson player keeps learner responses in React component state for the current browser session only.

- Moving backward and forward preserves the current session's single-choice and reflection responses.
- Restart asks for confirmation before clearing the current session state.
- Nothing is written to the backend.
- No `localStorage` or other durable browser persistence is used.

## 8. Accessibility behavior

The shell uses semantic headings, button controls, a labeled textarea, fieldset and radio-button semantics for the single-choice interaction, visible focus styles from the existing design system, an accessible step progress status, and focus movement to the current step heading where reasonably possible.

The layout uses responsive spacing and stacked controls so it remains usable at mobile width. It does not use automatic time limits and does not rely on color alone for meaning.

## 9. Feature-flag behavior

`APR_POC_ENABLED` remains the only feature flag source.

When APR is disabled, the backend returns 404 and the page displays:

`The APR technical proof of concept is disabled in this environment.`

No frontend feature flag was added.

## 10. Tests run

Local validation attempted or run during Day 3:

- Backend py_compile for APR files and APR tests.
- Backend ruff check for APR files and APR tests.
- Focused backend pytest command for `backend/tests/test_apr.py` where the environment permits Python 3.14 syntax and dependencies.
- Frontend lint.
- Frontend TypeScript checking.
- Focused APR frontend tests for the Day 2 route and Day 3 lesson player.

## 11. Tests blocked

This Codex environment may still block full backend pytest because the repository targets Python 3.14 while the local interpreter is Python 3.12, and backend dependency installation may depend on package-index access. The focused GitHub workflow uses Python 3.14 and is the expected backend validation path.

## 12. Systems deliberately not used

Day 3 deliberately does not use:

- Final Lesson 1 curriculum
- Portuguese teaching content
- Spanish explanations
- Audio
- Human recordings
- AI-generated audio
- Text-to-speech
- Microphone recording
- Speech-to-text
- Transcript editing
- Professor Gabriel
- AI prompts
- AI-generated feedback
- Evidence records
- Capability Observations
- Progress persistence
- Database migrations
- Learning rewards
- Grades
- Badges
- Missions
- Delayed review
- Subscriptions
- Billing
- Public deployment

## 13. Why the content is placeholder-only

The manifest explicitly identifies itself as `technical-placeholder` content and states:

- Technical placeholder lesson.
- Approved lesson content pending.
- This interaction tests the APR lesson player, not Portuguese capability.

It is not academically approved, not authorized for pilot, not authorized for public release, and replaceable by a future approved Lesson Specification.

## 14. Known limitations

- Only four technical step types exist.
- There is one fixed placeholder manifest.
- No durable progress or evidence is saved.
- The reflection field is session-only and disappears on browser reload or confirmed restart.
- The shell is not connected to audio, STT, TTS, LLM, or academic evidence workflows.
- Content remains neutral technical demonstration copy only.

## 15. Day 4 readiness

READY WITH CONSTRAINTS

The APR boundary can load and render a structured sequence with session-only interactions. Day 4 can build on this only after an approved Lesson Specification defines real academic content, evidence rules, and any permitted persistence model.
