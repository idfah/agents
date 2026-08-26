---
name: multi-agent-review
description: Use multiple subagents to perform an in-depth review.  Use only
  when asked to perform a multi-agent review.
---

# Multi-Agent Review

Use multiple agents to perform a detailed, in-depth review.  Multiple
subagents will perform narrowly scoped reviews and the top-level agent
will collate and summarize their responses.

If invoked without a specific target, review the current working changeset.

## Instructions

Use multiple subagents to review the requested target.  The top-level agent
will perform a comprehensive review while the subagents perform narrowly
scoped, individual reviews.  The top-level agent will then collate and
summarize all information into a final review.  Do not make changes to any
files; this is a review only.  The only possible exception to this rule is
if it is explicitly requested that a summary of the findings is written to
a file.

## Subagent Roles

Use custom subagent configurations whenever a configured agent matches the
requested role.  Select the custom agent by its configured name; avoid
recreating an available role by describing it in a generic subagent prompt.

Launch all subagents for a review in a single batch so they run in parallel.

Use these custom agents for the default review roles:
- Software Architect: `sw_architect`
- Repo Maintainer: `repo_maintainer`
- Software Tester: `sw_tester`

When the user requests an additional role, use a matching custom agent when
one is available.  For example, use `ml_engineer` for a requested machine
learning engineer review.  Use a generic subagent only when no suitable custom
agent exists.

Each subagent prompt must state the review target explicitly, because subagents
do not inherit the conversation.  Name the artifact, files, commits or diff
range under review and tell the subagent how to access it.

Subagents should only consider and report on issues that fall within the scope
of their defined role.

The default subagent roles are:
- Software Architect is focused only on high-level design and architecture.
- Repo Maintainer is focused on ensuring that the changes align with and follow
  the conventions, style, best practices, interfaces and overall design and
  spirit of the existing codebase.
- Software Tester is focused only on ensuring that software tests are accurate,
  valid, comprehensive and correct.  Tester is also focused on alignment of the
  tests with the repo test suite, including general scope and completeness of
  the new tests with respect to existing tests.

Different or additional agents may be used when requested.

## Subagent Structure

Subagents should return structured responses in a YAML-like `list[dict]` format:

- severity: The severity of the issue can be one of high, medium or low.
  description: The description of the issue, topic or potential problem that has
    been identified.
  proposal: A proposal for the preferred solution.
  compromise: A proposal for a second solution.  This may be a straightforward
    alternative or a less preferred or compromise solution.

The `severity`, `description` and `proposal` are required fields but
`compromise` is optional.

Subagents should report zero or more responses.  If they do not identify any
issues, it is OK to respond with "No issues identified."

Include this response format in each subagent prompt.

## Summary Response

The top-level agent should collate, summarize and evaluate the structured
responses returned by the subagents and incorporate it into the top-level
findings.  Then, the top-level agent should generate a summary report in the
form of an ordered list from highest severity to lowest severity.  The list
may also be grouped logically if it is appropriate or if the list is long.

The top-level agent should also suggest which findings warrant action and which
do not.

If requested, the top-level agent may write a checklist of the findings to
a file for later evaluation.

Report the summary as prose in the response.  Do not substitute a built-in
code-review or findings-reporting tool; those discard the severity, proposal
and compromise structure defined above.
