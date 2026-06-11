---
name: multi-agent-code-review
description: Use multiple subagents to perform an in-depth code review.  Use only when asked to perform a multi-agent code review.
---

# Multi-Agent Code Review

## Overview

Use multiple agents to perform a detailed, in-depth code review.  Multiple
subagents will perform narrowly scoped reviews and the top level agent
will collate and summarize their responses.

## Instructions

Review the requested changes using multiple subagents.  The top-level agent
will perform a comprehensive review while the sub-agents perform narrowly
scoped, individual reviews.  The top-level agent will then collate and
summarize all information into a final review.

The subagent roles are:
- Software Architect is focused only on high-level design and architecture
- Repo Maintainer is focused on ensuring that the changes align with and follow
  the conventions, style, best-practices, interfaces and overall design of the
  existing codebase.
- Caller's Perspective is focused on ensuring that new contributors to the
  codebase will be able to understand and use the changes.  Ensure that
  docstrings and comments are accurate, correct and complete.  Method and
  function names should make sense.  Documentation should be updated.  Behavior
  should batch stated intent and there should be no surprises.

Subagents should report only on issues that fall within the scope of their role.

Rules:

- Do not make any changes
- Rank issues by severity: low, medium or high
