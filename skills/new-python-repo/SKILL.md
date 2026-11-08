---
name: new-python-repo
description: Create Python repository scaffolding from bundled templates, or
  adapt existing files to those conventions when requested.  Use for starting
  a Python project or adding scaffolding around existing code.
---

# New Python Repo

Create a useful starting scaffold from [assets/](assets/).  Copy and adapt
the files directly; no generator or template engine is needed.

## Establish the Project

Inspect the conversation, target directory and applicable instructions first.
Gather the purpose, project title, distribution and import names, Python
support, dependencies and initial components.  Reuse information already
provided.  Ask focused questions one at a time for missing essentials rather
than running a fixed questionnaire or revisiting the template conventions.

Preserve existing Python requirements.  Otherwise use the local interpreter's
major/minor version as the minimum, without an upper bound.  Ask when the
choice is unclear.  Add runtime dependencies only when specified or clearly
established by the project; none are required for a fresh repo.  Preserve
supplied version constraints and otherwise leave dependencies unconstrained.
The default development extra contains build, pylint, pytest and sphinx.

## Copy and Adapt

Use a flat installable package unless existing structure or instructions
establish otherwise.  The assets include packaging, lint, test and Make
configuration, a package initializer, one import test, minimal repository
guidance and Sphinx documentation.  Add subpackages only when useful to the
project, with documented initializers and matching entries in the import test.

Replace these placeholders wherever they occur:

- `{{project_name}}`: human-readable project title.
- `{{distribution_name}}`: package distribution name.
- `{{package_name}}`: Python import package name; rename `assets/package/`
  accordingly when copying it.
- `{{description}}`: concise project description, adapted to its context.
- `{{python_version}}`: minimum supported Python major/minor version.

Adapt the Python requirement when preserving an existing range.  Set Pylint's
`py-version` to its minimum.  Quote and escape substituted values for their
file format, adjust RST heading underlines and wrap prose as needed.  Adapt
dependencies, package discovery, Make paths and documentation to the actual
layout.  Omit unknown license, author and hosting metadata; default the
initial version to `0.0.0`.

Use the bundled style guide and Pylint configuration as the baseline.
`docs/style.rst` is authoritative for coding conventions; AGENTS.md repeats
key guidance and describes the project.  Keep them aligned without expanding
the minimal README or AGENTS unnecessarily.

## Preserve Existing Work

Preserve existing README.md and AGENTS.md unless instructed otherwise.
Inspect every other destination before writing.  Add missing files and make
only clear, necessary adaptations to existing scaffolding; ask about uncertain
edits or meaningful conflicts.  Preserve files and functionality rather than
replacing an existing repo with the templates.  Do not move, delete or refactor
existing code merely to fit the scaffold.  Existing scripts may remain
unintegrated for follow-up work.

Leave virtual environments untouched.  Do not install dependencies or run
lint, tests, documentation builds or distribution builds during scaffolding.
Do not initialize Git, commit or publish unless requested.  The generated
commands and setup documentation are for later use.

## Follow-Up Adaptation

When explicitly asked to adapt an existing file to this scaffolding, inspect
the file and current repository and make targeted edits within that request.
For example, adapt AGENTS.md's layout, commands and style-guide references
while preserving project-specific guidance.  Ask about meaningful conflicts.
Do not treat a request to adapt one file as permission to rewrite others,
integrate existing code or execute the generated development commands.

## Finish

Review syntax, names, paths, documentation links and unresolved placeholders
without executing project code.  Summarize the files created or adapted,
existing content left untouched and useful follow-up work.  Distinguish this
review from installation or build verification, which has not been performed.
