---
name: ideation-qna
description: Conduct an adaptive, one-question-at-a-time ideation or refinement
  conversation and summarize the results.  Use only when the user explicitly
  asks to "play Q&A," "play N questions," "play questions and answers," or uses
  a close variant of those phrases.
---

# Ideation Q&A

Refine a topic by asking a sequence of relevant questions, discussing each
question until it is resolved, and synthesizing what the discussion means for
the topic.

## Start The Game

- Infer the topic from the request and conversation.  Ask for the topic before
  starting if it is not clear.
- Use the requested number of questions, or default to 10 when no number is
  given.
- Identify any requested downstream task, such as generating a plan or writing
  a document.  Use that purpose to guide the questions, but do not begin the
  downstream task during the Q&A phase.

## Ask Adaptive Questions

- Ask exactly one numbered question at a time using `Question X of N`.
- Choose each question using the topic, prior answers, current discussion and
  intended downstream task.
- Ask questions that improve clarity, insight, detail or refinement.  Explore
  goals, assumptions, constraints, alternatives, tradeoffs, risks and
  implications when they are relevant.
- Prefer focused questions over multi-part questions.  Avoid redundant
  questions and do not commit to a fixed list in advance.

## Resolve The Current Question

Treat each numbered question as an open discussion, not a single exchange.

- Advance directly when the user's answer clearly resolves the current
  question.
- When the user asks a question, requests elaboration, expresses uncertainty,
  disagrees or continues a tangent, respond without asking the next numbered
  question.
- Keep the current numbered question active through all related discussion.
  Do not count follow-up questions or readiness checks toward N.
- When it is ambiguous whether the discussion is resolved, ask whether the
  user is ready to continue.  Err toward waiting rather than advancing too
  early.
- Do not require a readiness check after an answer that is abundantly clear.
- Follow natural-language requests to skip, revisit, stop or add questions.
  If the user stops early, synthesize the discussion completed so far.

## Synthesize And Continue

After the final question and its discussion are resolved, print a concise,
task-dependent synthesis.  Organize it in the form most useful for the topic
rather than requiring fixed headings.  Capture the important conclusions,
explain what they mean and preserve material uncertainty or unresolved issues.

If the original request includes a downstream task:

- Print the synthesis before beginning that task.
- Proceed directly to the downstream task without another confirmation.
- Use the synthesis and full discussion as context for the downstream work.
- Do not let this skill broaden the actions authorized by the original request.

Write the synthesis to a file only when the user explicitly requests it.  Also
print the synthesis in the response unless the user explicitly requests
otherwise.
