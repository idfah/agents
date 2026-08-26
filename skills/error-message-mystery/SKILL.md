---
name: error-message-mystery
description: Play a read-only, one-mystery-at-a-time game that evaluates
  developer-facing errors and summarizes recommended improvements.  Use only
  when the user explicitly asks to "play error-message mystery," "play N
  error-message mysteries," or uses a close phrase that clearly names the
  game.  Do not use for ordinary debugging, review or error-handling requests.
---

# Error-Message Mystery

Evaluate whether code failures are understandable by presenting them as
mysteries for the user to diagnose.  Gather findings and recommendations, but
never make changes during the game.

## Start The Game

- Infer the target from the request and conversation.  Ask for it if unclear.
- Use the requested number of mysteries, or default to 5.
- Assume the user is a developer evaluating the target's error handling.
- Identify any requested downstream task, but do not begin it during the game.

## Investigate Read Only

- Inspect the target without modifying its code, tests, documentation,
  configuration or repository state.
- Prefer authentic errors from existing evidence or safe, side-effect-free
  reproduction.
- Do not run a reproduction that might alter data, repositories, external
  systems or production services.  When safety is uncertain or reproduction
  is impractical, simulate the error instead.
- Clearly label simulated errors and material traceback abbreviations.
- Record proposed improvements without implementing them or writing them to a
  file.

## Present One Mystery At A Time

- Adaptively choose relevant and non-redundant failure scenarios.
- Present exactly one `Mystery X of N` at a time.
- Show only what the developer would reasonably observe, such as the
  invocation, relevant context, error message and traceback.
- Do not reveal the cause before the user attempts a diagnosis.
- Ask what caused the failure and whether the diagnostic experience is
  acceptable.

## Resolve The Mystery

- Discuss the diagnosis and diagnostic quality until both are resolved.
- Treat successful diagnosis and diagnostic quality as separate decisions.  A
  solved mystery may still have a poor error message or traceback.
- Record a concise verdict and recommended change, allowing the result to fit
  the situation rather than requiring a fixed taxonomy.
- Advance directly when the discussion is clearly resolved.  When it remains
  ambiguous, ask whether the user is ready to continue.
- Do not advance when the user asks a question, requests elaboration or
  continues the discussion.
- Follow natural-language requests to skip, revisit, add mysteries or stop.  If
  the user stops early, summarize the mysteries resolved so far.

## Summarize And Continue

After the final resolved mystery, print a concise summary table with columns
for the mystery, failure scenario, diagnosis, diagnostic quality, verdict and
recommended change.  Follow it with useful cross-cutting conclusions and
unresolved issues.

If the original request includes a downstream task, print the summary before
beginning that task and pass the findings forward.  Follow the downstream
task's own authorization and safety requirements.  Agreement that something
should improve during the game does not authorize implementation.
