---
name: deep-lit-review
description: Perform a bounded literature review and record structured
  evidence cards drawn directly from primary sources.  Use only when the user
  explicitly asks for a "deep literature review."  Do not use for ordinary
  literature questions, background research or a lightweight review.
---

# Deep Literature Review

Search the literature on a topic, read the most relevant publications and
record structured evidence cards for later analysis and ideation.  Each card
describes what its source publication actually says.

This process is expensive.  Bound it deliberately.

## Establish The Brief

- Infer the topic from the request and current discussion.  Ask essential
  clarifying questions when a task-complete brief cannot be formed.
- Create a compact brief containing the question being investigated, the
  relevant scope, constraints and exclusions.
- Ask the caller for an output path when the request does not name one.
- Note the depth, which is the number of citation passes to allow.  Use two
  passes by default and never more than three.
- Allow about ten cards per pass unless the caller gives different numbers.
- Identify any requested downstream task, such as analysis, ideation or
  planning, but do not begin it during the review.

State the brief, the searches to be performed, the depth and the output path,
then begin.  Do not wait for approval; the caller can still interrupt.

## Read In Tiers

Read the way a careful reviewer reads, spending effort in proportion to
relevance:

- Screen roughly twenty candidates on title and abstract.  Write no cards at
  this stage.
- Read the abstract, conclusions and introduction of the relevant ones.
- Fully read the three or four publications that the conclusions of the review
  will rest on, including their methods and results.

Read this way in every pass.

Gather evidence only from a publication that was actually read:

- Never describe a publication based on how other work summarizes it.
- Never record a claim from a section that was not read.
- Read the abstract alone when the full text is unreachable, and record that
  only the abstract was read.
- Skip a publication entirely when nothing is reachable.

## Follow Citations

The first pass reads publications found by searching.  Each later pass reads
publications found in the references of the pass before it.

While reading, note references that look relevant to the brief.  After each
pass, follow only the references cited by two or more publications already
read, or load-bearing for a claim central to the brief.  When more references
qualify than the allowance permits, prefer the most widely cited among them
and then those closest to the brief.

- Read followed references in the same tiers as the first pass.
- Skip a reference that cannot be confidently matched to a specific document
  that was then actually read.  Never guess at the identity of a reference.
- Stop when no references qualify, when the allowed depth is reached or when
  the caller's card budget is exhausted.  The depth is a ceiling rather than a
  target, so a shallower review is a valid result.
- Do not record the candidate references anywhere; they are working notes for
  the next pass.

## Record Evidence Cards

Describe what the authors claim rather than whether they are correct.  The
scores are the reviewer's judgment; everything else comes from the
publication.

Record one card per publication using this structure:

```yaml
- title: The title of the publication
  pass: The citation pass this publication was found in
  id: A stable identifier such as a DOI or an arXiv id
  year: The publication year
  venue: The journal, conference or preprint server
  peer_reviewed: peer reviewed, preprint or unclear
  reference: A BibTeX entry for the publication
  read: abstract only, abstract and conclusions, or full text
  relevance: An integer from 1 to 10
  strength: An integer from 1 to 10
  strength_basis: One line explaining the strength score
  claims:
    - What the authors claim, one line each
  limitations:
    - Limitations the authors state and weaknesses evident in what was read
  factoids:
    - Concrete details worth remembering, such as settings or measurements
```

Judge `peer_reviewed` from the venue and take it as a best guess rather than a
verified fact.  Do not record citation counts.

Use 10 for relevance when a publication directly addresses the central
question of the brief, 5 when it is adjacent or partially relevant and 1 when
it is background only.

Use 10 for strength when a claim set is well supported and directly
demonstrated, 5 when it is plausible with substantial gaps and 1 when it is
asserted without support.  A card read from the abstract alone should not
exceed about 5, because rigor is not visible from an abstract.  Do not force a
particular score distribution.

End each claim with a short parenthetical naming the section it came from and
whether it was demonstrated or asserted, such as `(results, three datasets)`
or `(discussion, asserted)`.  Keep claims, limitations and factoids to one
line each.

## Write The File

Write one new YAML file at the agreed path containing the brief, the search
date, the searches performed, the depth, the summary and the cards:

```yaml
brief: The question being investigated
searched: The date the literature was searched
searches:
  - Each search or subtopic actually covered
depth_requested: The number of citation passes allowed
depth_reached: The number of citation passes actually completed
summary: The summary report
cards:
  - The evidence cards
```

The summary should cover what the sources agree on, where they disagree and
which gaps or approaches nobody appears to have tried.  Note how the cards
were distributed across the passes, and why the review stopped when the depth
reached is lower than the depth requested.  Also print the summary in the
response.

Write exactly one file and change nothing else.  Do not extend or merge with an
existing review.

If the original request includes a downstream task, print the summary before
beginning that task and pass the evidence forward.  Follow the downstream
task's own clarification, approval and safety requirements.
