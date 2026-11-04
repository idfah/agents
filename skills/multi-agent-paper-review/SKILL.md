---
name: multi-agent-paper-review
description: Review an academic paper or manuscript for publication using
  independent specialist reviewers and a combined publication recommendation.
  Use when asked for a multi-agent paper review or to assess a paper for
  publication using multiple reviewers.  Do not use for ordinary paper
  summaries or literature reviews.
---

# Multi-Agent Paper Review

Review a paper to understand its contribution, evaluate its technical merit,
identify shortcomings and provide constructive feedback to the authors.
Judge publication suitability against the supplied venue and its expectations.

This skill defines the complete paper-review workflow.  Use its reviewer roles,
response format and synthesis instructions directly.  Do not also invoke
`multi-agent-review`.

## Establish The Brief

Before proceeding, establish the following from the request or conversation:

- The paper to review and how to access it.
- The venue and a description of its scope and expectations.
- The directory where the final consolidated review will be saved.

Ask for any missing required information together before launching reviewers.
Accept optional author supplements, supporting code and reviewer-role overrides.
Save individual specialist reports only when the caller requests them.
State the brief and reviewer roster, then begin without another approval step.
Do not automatically inspect an unrelated context.

Ensure the whole paper is accessible, including equations, figures and tables
needed for the assessment.  Resolve missing or unreadable content before
claiming a whole-paper review.  If it cannot be resolved, explain the limitation
and ask how to proceed.

## Use Supporting Materials

The manuscript is the subject of review.  Author supplements and code are
auxiliary evidence that may clarify methods or establish a substantive
methodological concern.  Code quality, style and organization must not influence
the paper review.  Supporting code does not replace explanations needed in the
manuscript; distinguish implementation evidence from reporting omissions.

No agent may execute supplied code, reproduce experiments or run experiments
or scientific verification.  Agents may use utilities or generate and run code
solely to read, extract or parse documents.

When helpful, the parent may build document-reading tooling or prepare shared
reading artifacts once in a temporary location accessible to all reviewers.
This is optional; direct access to the original materials is sufficient.
Leave the approach and tooling to the parent's judgment.  Keep originals
available to resolve omissions or ambiguities in prepared artifacts.
Temporary reading artifacts are not required saved review outputs.

## Independent Specialist Reviews

Default to these predefined roles unless the caller supplies another roster:

- `ml_scientist`
- `mathematician`
- `statistician`

Use configured roles by name whenever available.  Use a suitably instructed
general agent only when no configured role matches.  If delegation is
unavailable, explain the limitation and ask whether to proceed with a
single-agent review.

Launch the specialists in parallel.  Do not pass the parent conversation or
other reviewers' findings.  Give each specialist the same neutral brief, the
paper and supporting-material locations, the relevant constraints and the
complete response format below.
If shared tooling or reading artifacts were prepared, include their paths and
any necessary usage instructions so reviewers can reuse them.  Independent
review means independent scientific assessment, not independent document
preparation.

Each specialist must independently read the entire paper and evaluate it
through their assigned role and expertise.  Each must provide all five ratings
and a publication recommendation within that scope.  Specialists return their
reports to the parent; they do not write review files.

Specialists must not search externally or fetch additional references.  Use
supplied materials and existing subject knowledge.  Flag particular references
or prior-work questions for the parent when they could materially affect the
assessment.

## Parent Assessment And Reference Checking

First consider the specialist reports, then read and assess the whole paper
with those reports available.  Check consequential criticisms against the
manuscript, consolidate overlapping findings and resolve material disagreements
through evidence and reasoning.  Preserve useful findings even when only one
specialist identifies them.  Do not average scores or decide by majority vote.

Keep external checking selective and bounded:

- Examine at most five external papers across the entire review.
- Prioritize papers cited by the manuscript and questions flagged by reviewers.
- Read abstracts by default.  Read relevant sections to resolve specific
  technical details.
- Perform at most one targeted search for uncited prior work, only when a
  central novelty or relevance claim warrants it.  Any resulting papers
  examined count toward the same five-paper limit.
- Do not follow citation chains or conduct a broader literature review.

The budget is a ceiling, not a target.  Distinguish comparisons verified against
sources from judgments based on existing knowledge.  If a question cannot be
resolved within these limits or sources are inaccessible, state the uncertainty
rather than expanding the search or treating the concern as established.

Combine the specialist findings with the parent's general assessment into a
final review using the same response format.  Explain how consequential
disagreements were resolved where relevant to the final judgment.  Preserve
meaningful unresolved disagreements and uncertainty in the final review.

## Response Format

Use the following format for every specialist report and the final review.
Keep the discussion high-level and readable; it does not need citations
throughout.  Support specific factual claims or criticisms when they arise.

### Summary

Write 1-3 short paragraphs summarizing what the authors are trying to achieve,
how they do it, why it matters and how it relates to previous research.  Be
brief and high-level; demonstrate that the reviewer understands the work.

### The Good

Write 1-3 short paragraphs describing what the authors have done well.
Consider what is novel, interesting and correct, any unique aspects of the
work and its contribution to the relevant scientific community.

### The Bad

Write 1-3 short paragraphs describing weaknesses, missing or inadequately
explained aspects, important evaluation gaps and high-level reproducibility
concerns.  Consider what the work adds beyond previous research.  Do not
invent shortcomings to fill this section.

### The Ugly

Include this section only when there are major concerns, using at most three
short paragraphs.  Examples include omissions that prevent assessment, errors
that invalidate central findings or missing evaluations essential to the
paper's claims.

Do not search for plagiarism.  If a clear concern is noticed incidentally,
describe the evidence and uncertainty without making an unsupported allegation.

### Ratings

Provide each score on a scale of 1-5: 1 is low or poor, 3 is neutral and 5 is
excellent.

- **Contribution:** What does the work contribute within the relevant field?
- **Novelty:** Is the contribution established, incremental or substantially
  new and valuable?  Consider scientific findings as well as methods.
- **Technical Quality:** Are the methods, assumptions and experiments
  appropriate and rigorous?  Does the evidence support the conclusions?
  Consider established practices without treating conformity as proof of merit.
- **Writing Quality:** Is the paper understandable and does it adequately
  explain the background, methods and experiments?  Assume another spelling
  and grammar pass will be made by the authors; consider such mistakes only
  when they affect understanding.
- **Overall Score:** What is the overall assessment of publication suitability
  for the supplied venue?

Also provide a **Publication Recommendation**: accept, minor revision, major
revision or reject.  Use venue-specific categories when the caller supplies
them.  Let the surrounding review and Specific Notes explain the scores and
recommendation; separate justifications for each score are not required.

### Specific Notes

Provide up to 30 substantive bullets with no minimum.  Prefer short, focused
notes, usually 1-2 sentences each; use up to 4 when helpful.  Use judgment about
grouping related concerns, favoring more focused notes over dense bullets.
The limit is not a target.  Each note should provide constructive feedback or
a specific unanswered question.

Ground each concern in evidence and identify the relevant page,
section, equation, figure, table or cited work so the authors can locate it.
For missing information, identify the relevant section and explain what is
missing.  Distinguish demonstrated errors, unclear reporting and suggestions
for improvement.

Consider suspect claims, wording that affects understanding, important missing
analyses and material that could be omitted or replaced to improve focus.
Assume the authors will revise regardless of the publication decision.
Respect length restrictions and keep requests proportionate to the paper's
claims.  Distinguish essential revisions from optional future work rather
than requesting large amounts of additional experimentation.

## Save The Reports

The parent always saves the consolidated report as `paper_review.md` in the
caller's specified directory unless the caller specifies another filename.
Create that directory if needed.  Save individual specialist reports as
`<agent_role>_review.md` only when the caller requests them.  Number filenames
when roles repeat.
Ask before overwriting existing reports unless replacement is already
authorized.  Do not modify the manuscript, supporting code or other source
materials.

In the final response, briefly state the publication recommendation and link
to the consolidated review.  Also link to individual reports when saved.
