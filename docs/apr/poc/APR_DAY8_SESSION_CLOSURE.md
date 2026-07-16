# APR Day 8 Session Closure

## 1. Goal
Day 8 turns the APR technical lesson flow into a coherent founder-testable browser session with a controlled end screen and a session-only technical summary.

## 2. Branch
`codex/apr-day8-session-closure-staging`

## 3. Why session closure is outside the five-step manifest
The closure screen is generic lesson-player shell behavior. It is not instructional content, not a sixth academic step, and not Lesson or Module completion.

## 4. Manifest version
The manifest version is `0.6.0-technical-placeholder`; `current_step_count` remains `5`.

## 5. Exact closure copy
- Heading: `Technical session ready for review`
- Main explanation: `You reached the end of this technical prototype. This summary describes browser-session activity only. It is not lesson completion, Progress, Evidence, a score, or a language result.`
- Status label: `Session-only technical summary`
- Next action: `Next: review your session, restart the technical flow, or exit to the APR module.`

## 6. Summary rows
- Original recording
- Original transcript
- Latest retry
- Technical model audio
- Controlled technical feedback
- Post-feedback retry

## 7. Controlled summary values
- Original recording: Captured, Not captured
- Original transcript: Confirmed, Not confirmed
- Latest retry: Captured, Not captured
- Technical model audio: Generated, Not generated, Technical issue
- Controlled technical feedback: Ready, Not requested, Technical issue
- Post-feedback retry: Captured, Not captured, Not applicable

## 8. How each value is derived
Values come only from current `AprLessonPlayer` state: protected Original Blob, Original confirmed transcript plus positive revision, Latest retry Blob, model-audio status, current feedback status tied to the current Original confirmation revision, and the retry-sequence snapshot.

## 9. No backend summary request
No summary endpoint is called.

## 10. No completion endpoint
No completion endpoint exists or is called.

## 11. No persistence
The summary is not saved to a database, filesystem, object storage, localStorage, or IndexedDB.

## 12. No Progress
No Progress write is created.

## 13. No Evidence
No Evidence write is created.

## 14. No score
No score is calculated or displayed.

## 15. No language result
The closure does not report proficiency, correctness, pronunciation, fluency, grammar, or improvement.

## 16. Reflection-state handling
Reflection text remains in the existing session response state so it survives movement between reflection and closure. Confirmed Restart clears it. It is not shown in the summary or sent to the backend.

## 17. Back to reflection
`Back to reflection` hides closure and returns to the final reflection step without resetting session state.

## 18. Restart
`Restart technical session` uses the existing confirmation dialog. Cancel preserves closure and session state; confirm clears governed state and returns to step one.

## 19. Exit
`Exit to APR module` routes to `/apr/primeira-conexao` without sending completion, Progress, or Evidence.

## 20. Unmount
Unmount aborts active transcript, model-audio, and feedback requests and uses the existing object-URL cleanup rules.

## 21. Strict Mode
Closure is entered only by explicit final Continue. Request generations, mounted refs, abort controllers, and object-url refs keep stale responses from attaching.

## 22. Accessibility
The closure has one focused heading, real buttons, semantic description-list summary markup, visible text statuses, and no focus trap.

## 23. Mobile behavior
The summary uses a responsive grid and wrapping text so status labels remain readable at mobile width.

## 24. Tests run
Frontend lint, TypeScript checking, and the focused APR frontend Vitest command passed locally with 7 files and 73 tests. Backend Ruff and APR compile checks passed locally.

## 25. Tests blocked
Python 3.14 pytest was blocked locally because dependencies were not installed for `PYENV_VERSION=3.14.4`, and `python -m pip install -r requirements.txt` could not reach package indexes due a 403 network tunnel response. The APR GitHub workflow remains configured to install dependencies and run `pytest tests/test_apr.py -v --no-cov` on Python 3.14.

## 26. Known limitations
The content is still technical placeholder material. Model audio and feedback are not final academic assets.

## 27. Founder-test readiness
READY WITH CONSTRAINTS: browser flow is ready, but a private hosted URL depends on operator deployment.

## 28. Day 9 readiness
READY WITH CONSTRAINTS: the shell is ready for real Lesson 1 content, but Day 9 must supply approved content and audio.
