---
name: code-context-warmup
description: Inspect, analyze and summarize code components to build working context before making changes.  Use when asked to warmup by inspecting or analyzing code.  Only trigger when the word "warmup" is explicitly mentioned.
---

# Code Context Warmup

Inspect and summarize the requested material.  The goal of this process is to
build a working context around code or other material that will be the
subject of subsequent discussion, implementation, refactors or other changes.


## Instructions

Inspect the coder or other material in order to explain, describe and summarize:

- What these components do and what is their purpose at a high level.
- Why they appear to exist.
- How they interact and how changes might break their interaction.
- Public contract versus internal implementation detail.
- Invariants and assumptions at a high level.
- Behaviors that are easy to break.
- Tests or call sites that should be checked before changing anything.
- Overall behavior, design and intent.
- High-level architecture and interaction.

At the end of the summary, include a brief list of questions describing aspects
of the code or other material that cannot be clearly inferred or that might
seem ambiguous.

## Rules

- Do not make any changes; this is a warmup task only.  The only possible
  exception to this rule is if it is explicitly requested that the summary
  is written to a file.
- Read the actual implementation and nearby call sites instead of guessing.
- Keep the description high-level and brief unless the user asks for more.
- Distinguish public contract from internal detail.
- Preserve and identify the original intent of the code in the summary.
- Check nearby tests when they provide evidence about intended behavior.
- Check relevant repository documentation and design documents for additional
  information and context.
- State uncertainty clearly when the code does not provide enough evidence.
