---
name: plan-changes
description: Make a plan or generate a revised plan to implement a code change.
  Use when asked to plan, or to revise a plan for, a set of changes before
  implementing them.
---

# Make A Plan

Generate a plan or revise a previous plan to implement changes.  The goal of
making a plan is to better define and describe what will be done during when
asked to implement the changes.

If invoked without a specific target, plan the changes that are the current
subject of the conversation.

## Preparation Steps

Before generating a plan consider the following:
- Carefully consider what is being asked and how it fits into the
  context of the broader and previous conversational context.
- Is there context information that should be reviewed?  For example, relevant
  code, design documents, repo documentation, external links and resources.
  If so, review this information for relevant details.
- Think about how the requested changes fit and align with the rest of the
  respository.

Before generating the plan, identify any unresolved questions or ambiguities
that could materially affect it.  Discuss these with the user first, preferably
together in a concise conversational form.  Delay the full plan until they are
resolved or the user asks you to proceed using stated assumptions.

## Make A Plan

The plan should contain of a step-by-step list of items to be done in order
to implement the requested changes.  The plan should be human readable and
concise enough to be easily and quickly reviewed before the changes take place,
while also describing the full scope of the changes and what will be done.

If it seems like the requested changes are large, suggest that it could be
done across multiple vertical slices.

Always include:
- A summary of anything ambiguous, remaining questions or anything that might
  be a potential source of issues.
- Describe what would be done if no further clarification is provided for
  each listed ambiguity or remaining open questions.

When appropriate, optionally include:
- Short code snippets or sketches describing how things will look
- Steps that will be taken to validate or test the changes are correct
- Suggestions and assumptions about potential ambiguities.

## Rules

- Do not make any changes; this is a planning step only.  The only possible
  exception to this rule is when it is explicitly requested that the plan is
  written to a file.
- Present the plan in the response.  Do not enter a plan-approval mode unless
  the user asks for one.
