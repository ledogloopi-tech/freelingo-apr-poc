---
description: "Frontend architecture reference for FreeLingo: directory structure, pages, components, state management, utilities, code standards, page content width convention, and test configuration."
applyTo: "frontend/**"
---

# Architecture — Frontend

> The general architecture overview (repository structure, data flows, auth design) lives in [architecture.instructions.md](architecture.instructions.md). Backend-specific architecture lives in [architecture-backend.instructions.md](architecture-backend.instructions.md).

## Directory structure

```
frontend/
├── src/
│   ├── app/
│   │   ├── (auth)/              # Public routes (7 pages)
│   │   │   ├── billing/         # Stripe-managed billing (redirect)
│   │   │   ├── forgot-password/
│   │   │   ├── login/
│   │   │   ├── onboarding/      # Post-registration language + level setup
│   │   │   ├── register/
│   │   │   ├── reset-password/
│   │   │   └── verify-email/
│   │   │
│   │   ├── (app)/               # Authenticated routes — sidebar layout (19 pages)
│   │   │   ├── layout.tsx       # Sidebar + global layout shell
│   │   │   ├── loading.tsx
│   │   │   ├── admin/           # Admin overview + admin-only management routes
│   │   │   ├── admin/users/     # User list + [id] detail: tabs, quotas, subscription override
│   │   │   ├── admin/feedback/  # Feedback queue admin panel: search, filters, responsive table/cards
│   │   │   ├── admin/reviews/   # Review moderation: filters, approve/unapprove, delete
│   │   │   ├── assessment/      # Level test: BeginnerGate → AdaptiveQuizCard → DurationSelector
│   │   │   ├── chat/            # AI tutor SSE chat + conversation history
│   │   │   ├── conversation/    # Real-time voice conversation (WebSocket + VAD)
│   │   │   ├── dashboard/       # Home: XP, streak, plan summary, language selector
│   │   │   ├── faq/             # Frequently asked questions
│   │   │   ├── feedback/        # Feature requests & bug reports board
│   │   │   ├── flashcards/      # Spaced-repetition flashcard review
│   │   │   ├── grammar/         # Grammar reference (index + [slug] detail)
│   │   │   ├── lesson/[id]/     # Lesson player with exercises
│   │   │   ├── listening/       # AI-generated listening exercises
│   │   │   ├── phrasebook/      # Common phrases by category
│   │   │   ├── plan/            # Study plan overview + unit drawer
│   │   │   ├── progress/        # Skills tracker with radar chart
│   │   │   ├── reading/         # AI-generated reading comprehension
│   │   │   ├── settings/        # Profile, avatar, subscription, conversation config
│   │   │   └── vocabulary/      # Vocabulary hub (index + [setId] detail)
│   │   │
│   │   ├── (legal)/             # Minimal layout (2 pages)
│   │   │   ├── layout.tsx
│   │   │   ├── privacy/
│   │   │   └── terms/
│   │   │
│   │   └── api/                 # Next.js Route Handlers (proxies to backend)
│   │       ├── chat/route.ts    # SSE chat streaming proxy
│   │       ├── stt/route.ts     # STT proxy
│   │       └── tts/route.ts     # TTS proxy
│   │
│   ├── components/              # 12 directories + 5 standalone files
│   │   ├── assessment/          # AdaptiveQuizCard, BeginnerGate, DurationSelector
│   │   ├── admin/               # AdminNav + AdminShell primitives shared across admin pages
│   │   ├── billing/             # Stripe subscription UI components
│   │   ├── chat/                # Chat message components
│   │   ├── conversation/        # ConversationMode, MicButton, StatusIndicator, TranscriptBubble...
│   │   ├── flashcard/           # Flashcard review components
│   │   ├── lesson/              # Lesson exercise components
│   │   ├── plan/                # LevelTestBanner, UnitCard, UnitDrawer
│   │   ├── reviews/             # ReviewPrompt, reusable ReviewForm, landing reviews carousel
│   │   ├── settings/            # Settings form components, including profile review section
│   │   ├── tour/                # OnboardingTour components
│   │   ├── ui/                  # shadcn/ui + custom: AudioPlayer, VoiceRecorder, confirm-dialog...
│   │   ├── whats-new/           # What's New changelog modal
│   │   ├── CookieBanner.tsx
│   │   ├── LanguageSwitcher.tsx
│   │   ├── TargetLanguageText.tsx # Language-aware typography wrapper for learned-language content
│   │   ├── TargetLanguageSelector.tsx
│   │   └── ThemeProvider.tsx
│   │
│   ├── data/                    # Static content: curriculum, grammar, phrasebook — vocabulary + assessment now in backend
│   │   ├── types.ts              # Shared TypeScript types (CEFRLevel, AssessmentQuestion, VocabularyEntry, VocabularySet, etc.)
│   │   ├── curriculum.ts         # Curriculum definitions — language-aware dispatcher (API-backed)
│   │   ├── grammar.ts            # Grammar reference — language-aware dispatcher
│   │   ├── phrasebook.ts         # Phrasebook — language-aware dispatcher
│   │   ├── en/                   # English (3 files: curriculum, grammar, phrasebook)
│   │   ├── es/                   # Spanish (3 files)
│   │   ├── it/                   # Italian (3 files)
│   │   └── pt/                   # Portuguese (3 files)
│   │
│   ├── store/                   # Zustand stores (6)
│   │   ├── auth.ts              # Access token, user info, login/refresh/logout
│   │   ├── config.ts            # Public config: maintenance mode, feature flags, languages
│   │   ├── language.ts          # UI locale + target language state
│   │   ├── loading.ts           # Global loading spinner state
│   │   ├── progress.ts          # XP, streak, skill scores, dashboard data
│   │   └── theme.ts             # Dark/light/system theme
│   │
│   ├── lib/                     # Utility modules (10)
│   │   ├── api.ts               # apiFetch: auth interceptor, 401 → silent refresh → retry
│   │   ├── audio.ts             # Audio player, audio queue, gapless playback helpers
│   │   ├── conversation-ws.ts   # WebSocket client for voice conversation
│   │   ├── landing-subscription.ts # Shared landing subscription-status check
│   │   ├── locales.ts           # Locale utilities for next-intl
│   │   ├── mappers.ts           # Data transformation / mapping utilities
│   │   ├── reviews.ts           # Review API client helpers
│   │   ├── target-languages.ts  # Target language definitions and helpers
│   │   ├── utils.ts             # General utility functions
│   │   └── review-prompt-triggers.ts # Review prompt trigger rules for voice sessions and unit completion
│   │
│   ├── i18n/
│   │   └── request.ts           # next-intl request locale resolver
│   │
│   └── middleware.ts            # Auth guard (redirect to /login) + locale detection
│
├── tests/                       # Vitest suite (30 test files, 399 tests; coverage not configured)
│   ├── setup.ts                 # Global mocks: localStorage, next/navigation, next-intl
│   ├── middleware.test.ts
│   ├── components/
│   │   ├── LanguageBubbles.test.tsx
│   │   ├── LanguageSwitcher.test.tsx
│   │   └── TargetLanguageSelector.test.tsx
│   ├── data/
│   │   └── curriculum.test.ts
│   ├── lib/
│   │   ├── api.test.ts
│   │   ├── audio.test.ts
│   │   ├── conversation-ws.test.ts
│   │   ├── mappers.test.ts
│   │   └── target-languages.test.ts
│   └── store/
│       ├── auth.test.ts
│       ├── config.test.ts
│       └── language.test.ts
│
├── public/                      # Static assets
│   ├── apple-touch-icon.png
│   ├── favicon.ico
│   ├── favicon.png
│   ├── github.svg
│   ├── github_white.svg
│   ├── logo.png
│   ├── og-image-v2.png
│   ├── flags/                   # Language flag SVGs
│   └── vad/                     # Silero VAD ONNX models for browser WASM
│
├── messages/                    # i18n message bundles (en, es, fr, pt, de, it, nl, pl, ro, ru)
│   ├── en.json
│   ├── es.json
│   └── ...
│
└── scripts/
    └── copy-vad-models.js       # Postinstall: copies VAD WASM models to public/
```

## Page routes

### Public (auth) routes — `(auth)/`

| Route              | Description                                             |
| ------------------ | ------------------------------------------------------- |
| `/login`           | Email + password login                                  |
| `/register`        | Registration form with native/target language selection |
| `/onboarding`      | Post-registration: language preferences + level setup   |
| `/verify-email`    | Email verification token handler                        |
| `/forgot-password` | Request password reset email                            |
| `/reset-password`  | Reset password with token                               |
| `/billing`         | Stripe Customer Portal redirect (managed by Stripe)     |

### Authenticated routes — `(app)/`

- `/dashboard` — Home: XP counter, streak, next lesson card, target language selector.
- `/assessment` — Level placement test (`BeginnerGate` → `AdaptiveQuiz` → `DurationSelector`).
- `/plan` — Study plan overview: unit cards, `LevelTestBanner`, `UnitDrawer`.
- `/lesson/[id]` — Lesson player: content + interactive exercises. Completing a lesson may open the reusable review prompt when it advances the user out of the completed curriculum unit, subject to duplicate-review checks and local dismissal cooldown.
- `/chat` — AI tutor text chat with SSE streaming.
- `/conversation` — Real-time voice conversation with WebSocket + VAD. When the user manually stops a connected voice session after at least 5 minutes, the page may open the reusable review prompt, subject to duplicate-review checks and local dismissal cooldown.
- `/flashcards` — Spaced-repetition flashcard review.
- `/grammar` — Grammar reference index.
- `/grammar/[slug]` — Grammar topic detail page.
- `/vocabulary` — Vocabulary hub overview.
- `/vocabulary/[setId]` — Vocabulary set detail.
- `/phrasebook` — Common phrases by category.
- `/listening` — AI-generated listening comprehension exercises.
- `/reading` — AI-generated reading comprehension exercises.
- `/progress` — Skills tracker with radar chart and multi-level vocabulary progress toggle.
- `/settings` — Profile, avatar, subscription, user review creation/editing, conversation settings.
- `/faq` — Frequently asked questions.
- `/admin/reviews` — Admin-only review moderation with status/rating filters, approve/unapprove, and delete confirmation.
- Landing page — The top navigation includes a Reviews anchor between Features and Pricing when approved public reviews are available; the same conditional link appears in the mobile menu. Review carousel cards keep a consistent height and clamp long comments to 6 lines.
- `/feedback` — Feature requests and bug reports board (community).
- `/admin` — Admin overview with aggregated metrics including pending feedback and pending review approvals, operational alerts, quick links to users/feedback/reviews, and maintenance-mode status (admin only).
- `/admin/users` — User management with responsive table/cards, search, filters, invite copy workflow, create-user sheet, and maintenance toggle (admin only).
- `/admin/users/[id]` — Admin user detail with summary header and tabs for Profile, Languages, Activity, Quotas, and Subscription. Quotas separate current usage from configured limits; email verification and subscription overrides use confirmation dialogs.
- `/admin/feedback` — Feedback queue admin panel with search, type/status/sort filters, filtered metrics by feedback type, desktop table, mobile cards, status updates, and delete confirmation. Status updates refresh the queue when the updated entry no longer matches the active filter (admin only).

### Legal routes — `(legal)/`

| Route      | Description      |
| ---------- | ---------------- |
| `/privacy` | Privacy policy   |
| `/terms`   | Terms of service |

### API route handlers

These are Next.js Route Handlers that proxy requests to the backend:

| Route       | Method | Purpose                  |
| ----------- | ------ | ------------------------ |
| `/api/chat` | POST   | SSE chat streaming proxy |
| `/api/tts`  | POST   | Text-to-speech proxy     |
| `/api/stt`  | POST   | Speech-to-text proxy     |

## State management (Zustand)

Six Zustand stores hold all client-side state. No React Context is used for global state.

| Store      | Persisted?         | Key state                                                                                      |
| ---------- | ------------------ | ---------------------------------------------------------------------------------------------- |
| `auth`     | No (JS memory)     | `accessToken`, `user`, `isAuthenticated`, `login()`, `refresh()`, `logout()`                   |
| `config`   | No                 | `maintenanceMode`, `availableLanguages`, `stripeEnabled`, feature flags from `GET /api/config` |
| `language` | Yes (localStorage) | `targetLanguage` (BCP-47), `uiLocale`, language switcher state                                 |
| `loading`  | No                 | `isLoading`, `startLoading()`, `stopLoading()` — global spinner control                        |
| `progress` | No                 | `xp`, `streak`, `skillScores`, `planSummary` — fetched from backend                            |
| `theme`    | Yes (localStorage) | `"light"` / `"dark"` / `"system"`                                                              |

## Utility modules (`lib/`)

- **`api.ts`** — Fetch wrapper with auth interceptor: injects `Authorization` header, catches 401 → silent refresh → retry, redirects to `/login` on refresh failure
- **`audio.ts`** — Audio playback queue for voice conversation; tracks real queue idle state so the UI clears "speaking" only after playback drains
- **`conversation-ws.ts`** — WebSocket client for the voice conversation pipeline, handles WAV chunk sending and MP3 reception
- **`landing-subscription.ts`** — Shared landing-page subscription check used by `LandingNav` and `PricingSection`; deduplicates refresh + `/api/auth/me` so the nav hides `Pricing` whenever the pricing section is hidden for active/trialing subscribers
- **`locales.ts`** — next-intl locale detection and routing utilities
- **`mappers.ts`** — Data transformation helpers between API responses and frontend models
- **`target-languages.ts`** — Target language definitions: BCP-47 codes, display names, flag mappings, ISO codes, script/romanisation metadata, word-spacing capability, and language-specific font class helpers. The public `SUPPORTED_TARGET_LANGUAGES` list controls which languages are selectable; CJK capabilities may be defined ahead of activation.
- **`utils.ts`** — General-purpose utilities: formatting, date helpers, class name merging

## Components overview

### Page-specific components

| Directory       | Key components                                                                                     |
| --------------- | -------------------------------------------------------------------------------------------------- |
| `assessment/`   | `AdaptiveQuizCard`, `BeginnerGate`, `DurationSelector`                                             |
| `admin/`        | `AdminNav`, `AdminPageHeader`, `AdminPanel`, `AdminMetric`, `AdminBadge` shared across admin pages |
| `billing/`      | Stripe subscription management UI; landing `PricingSection` hides for active/trialing subscribers  |
| `chat/`         | Message display, input, SSE stream handling                                                        |
| `conversation/` | `ConversationMode`, `MicButton`, `StatusIndicator`, `TranscriptBubble`, VAD integration            |
| `flashcard/`    | Flashcard flip animation, SM-2 rating buttons                                                      |
| `lesson/`       | Exercise renderers (multiple choice, fill-in-blank, listening, reading)                            |
| `plan/`         | `LevelTestBanner`, `UnitCard`, `UnitDrawer`                                                        |
| `settings/`     | Profile form, avatar upload, conversation preferences                                              |
| `tour/`         | `OnboardingTour` step-by-step walkthrough                                                          |
| `whats-new/`    | Version-aware changelog overlay modal                                                              |

### Shared/generic components

- **`ThemeProvider.tsx`** — Dark/light/system theme via `next-themes`
- **`TargetLanguageSelector.tsx`** — Language picker dropdown with flags
- **`TargetLanguageText.tsx`** — Reusable wrapper for content in the learner's target language. It applies `lang`, language-aware typography classes from `target-languages.ts`, and optional secondary reading/translation lines for future romanisation/pinyin support.
- **`LanguageSwitcher.tsx`** — UI locale switcher
- **`CookieBanner.tsx`** — GDPR cookie consent banner
- **`ui/`** — shadcn/ui primitives (`button`, `card`, `input`, `progress`, `badge`, `separator`, `sheet`, `tabs`) + custom: `AudioPlayer`, `VoiceRecorder`, `confirm-dialog`

---

## Code standards (TypeScript / Next.js 16)

| Tool     | Purpose                                         |
| -------- | ----------------------------------------------- |
| ESLint   | TypeScript linting + Next.js rules              |
| Prettier | Code formatting + `prettier-plugin-tailwindcss` |

- No semicolons, single quotes, 2-space tabs, trailing commas "es5".
- shadcn/ui components installed: `button card input progress badge separator sheet tabs`.

### Page content width convention

Every page wrapper uses `mx-auto` plus one of three canonical widths. Do not use other sizes:

| Class       | Width   | Use for                                                                                                    |
| ----------- | ------- | ---------------------------------------------------------------------------------------------------------- |
| `max-w-6xl` | 1152 px | Dense admin data pages and operational admin overview (admin, admin/users, admin/feedback)                 |
| `max-w-5xl` | 1024 px | Admin overview pages with lighter operational cards                                                        |
| `max-w-4xl` | 896 px  | Index/overview pages with grids or card layouts (dashboard, grammar, vocabulary, phrasebook, progress)     |
| `max-w-3xl` | 768 px  | Compact detail or legacy admin list pages                                                                  |
| `max-w-2xl` | 672 px  | Detail pages, forms, long-form content (lesson, grammar detail, settings, feedback, flashcards, faq, plan) |

Full-screen interactive experiences (conversation, chat, listening, reading, assessment) are exempt — they manage their own layout internally.

### Target-language typography

The global FreeLingo visual language remains mono-heavy: `Geist`/`Geist_Mono` are loaded in `src/app/layout.tsx`, and `globals.css` maps the default theme fonts to the mono variable. Do not change this globally when adding non-Latin target languages.

Content that is part of the language being learned must use the language-aware rendering path instead of raw `font-mono` text:

- `frontend/src/lib/target-languages.ts` stores `script`, `fontClass`, `usesWordSpacing`, and optional `romanization` metadata.
- `getTargetLanguageTextClass(code)` returns Latin-compatible mono styling for current Latin-script languages and CJK-friendly `font-target-ja`, `font-target-ko`, or `font-target-zh` classes for future `ja-JP`, `ko-KR`, and `zh-CN`.
- `frontend/src/components/TargetLanguageText.tsx` applies the correct class and `lang` attribute. Use it for lesson content, exercise prompts/options, flashcards, reading/listening transcripts, phrasebook entries, vocabulary examples, assessment questions, and chat/conversation transcript text.
- `globals.css` defines `font-target-latin`, `font-target-ja`, `font-target-ko`, and `font-target-zh`. CJK classes use Noto variables when available plus platform fallbacks (`Hiragino Sans`/`Yu Gothic`/`Meiryo`, `Apple SD Gothic Neo`/`Malgun Gothic`, `PingFang SC`/`Microsoft YaHei`/`Noto Sans CJK SC`).

UI labels, levels, controls, navigation, and admin chrome may continue using `font-mono`, `uppercase`, and wide tracking. Do not apply `uppercase`, `tracking-widest`, or small mono text to learned-language CJK content.

---

## State flow — Auth interceptor

```
Any fetch via apiFetch()
    ↓
Add Authorization: Bearer <accessToken>
    ↓
Request succeeds? → return response
    ↓ 401 received
Silent call to POST /api/auth/refresh
    ↓
Refresh succeeds? → store new accessToken, retry original request
    ↓
Refresh fails? → clear auth store, redirect to /login
```

---

## State flow — SSE chat streaming

```
User sends message → POST /api/chat (SSE proxy)
    ↓
Next.js Route Handler forwards to backend SSE endpoint
    ↓
Backend: LLM Adapter streams tokens → SSE events
    ↓
Frontend receives SSE events:
  - token events → append to message accumulator
  - done event → finalize message, add to ChatHistory
  - error event → show error, stop streaming
```

---

## State flow — WebSocket voice conversation

```
User opens /conversation → load VAD WASM models
    ↓
WebSocket connects: new WebSocket(`/ws/conversation`)
    ↓
Client sends first JSON auth frame with access token, voice preference, target language, and optional chat context
    ↓
VAD detects speech → send WAV chunks via WS
    ↓
Server: STT → full LLM response → sentence-level TTS chunks
    ↓
Receive MP3 binary frames via WS → AudioQueue schedules playback in order
    ↓
AudioQueue drains → clear assistant speaking state from playback `onIdle`
```

`ConversationMode` guards the session lifecycle with a per-start attempt id. If microphone startup fails, the user stops the session, or the component unmounts while the warmup request is still pending, the pending attempt is invalidated so it cannot open a stale WebSocket afterwards.

The voice UI does not clear `assistantSpeaking` from `turn_complete` or `status=listening`; it waits for the audio queue idle callback so the visible speaking state follows actual playback. A separate assistant-turn guard ignores VAD detections while the tutor is generating or sending chunked audio, so automatic frontend barge-in remains disabled for stable turn completion while the backend `barge_in` protocol stays available.

## Tests

Testing infrastructure and strategy are documented in [testing.instructions.md](testing.instructions.md).

**Summary:**

- **Framework**: Vitest with jsdom environment
- **Test files**: 30 (plus setup.ts) covering critical logic only
- **Setup**: Global mocks for `localStorage`, `next/navigation`, `next-intl`
- **Coverage areas**: API fetch interceptor, auth store, audio queue, conversation WebSocket, target language utilities, mapper functions, middleware, component rendering
- **Coverage**: Not configured/reported (`@vitest/coverage-v8` is not installed)
