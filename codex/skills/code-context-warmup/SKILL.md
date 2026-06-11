---
name: code-context-warmup
description: Inspect, analyze and summarize code components to build working context before making changes.  Use when asked to warmup by inspecting or analyzing code.  Only trigger when the word "warmup" is explicitly mentioned.
---

# Code Context Warmup

## Overview

Inspect and summarize the requested code to build working context so
future changes preserve existing interfaces, APIs, behavior, and
invariants.

## Instructions

Inspect the code in order to explain, describe and summarize:

- What these components do at a high level
- Why they appear to exist
- How they interact and how changes might break their interaction
- Public contract versus internal implementation detail
- Invariants and assumptions at a high level
- Behaviors that are easy to break
- Tests or call sites that should be checked before changing anything
- Overall behavior, design and intent

Rules:

- Do not make any changes
- Read the actual implementation and nearby call sites instead of guessing
- Keep the description high-level and brief unless the user asks for more
- Distinguish public contract from internal detail
- Preserve and identify the original intent of the code in the summary
- Check nearby tests when they provide evidence about intended behavior
- State uncertainty clearly when the code does not provide enough evidence
