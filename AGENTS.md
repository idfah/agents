# Agent Configurations

This repository contains the public source configuration for my coding
assistants and agentic workflows.  Keep secrets, proprietary information,
repository-specific paths and machine-specific permissions out of this
repository.

## Repository Structure

- `codex/` contains Codex instructions and a complete baseline `config.toml`.
- `claude/` contains Claude instructions and a complete baseline `settings.json`.
- `skills/` contains shared skills.  Codex-specific `agents/openai.yaml` files
  remain co-located with their corresponding skills.
- `subagents/` contains canonical Markdown subagent role descriptions with
  separate `claude` and `codex` configuration sections.
- `scripts/install` installs one tool's configuration.
- `tests/` contains focused installer tests.

Write shared skill and subagent instructions so they stay harmless on a tool
that lacks the feature being described, rather than dropping them.  Describe
what to do and which agents to use, not how a tool discovers or loads its own
configuration.  Isolate native configuration in the existing tool-specific
files and metadata sections.

## Installation

Run `scripts/install codex` or `scripts/install claude`.  The installer uses
`~/.codex` and `~/.claude`, respectively.

Normal installation overwrites managed instructions, same-named skills and
same-named subagents.  It leaves unrelated and obsolete local files untouched.
It installs `config.toml` or `settings.json` only when missing; `--force`
overwrites all managed files, including that configuration.  `--dry-run` reports
planned changes without writing.

The installer requires Python.  Install its unpinned runtime and development
dependencies with `pip3 install -r requirements.txt`.

## Python Style

- Follow PEP 8 unless a rule below overrides it.
- Do not use all-caps variable names, including module globals.
- Do not use type hints.
- Do not use double blank lines.
- Target a soft line length of 90 characters and a hard maximum of 100.
- Prefer single quotes for strings and double quotes for docstrings.
- Prefer f-strings and format-style interpolation; do not use `%` formatting.
- Name caught exceptions `ex`.
- Group standard-library, third-party and local imports, with one blank line
  between groups.
- Keep imports alphabetized within each group.
- Prefer module and namespace imports over direct symbol imports.
- Do not use wildcard imports.
- Use `pathlib` for filesystem paths.
- Single-line comments do not end with a period; multi-line or multi-sentence
  comments do.
- Modules, classes and functions must have docstrings.
- Use Google-style docstrings.  Document argument and return types without
  adding Python type hints.
- Put each argument or return name and type on its own line, with the
  description on the following indented line.
- Put the closing quote of every docstring on its own line.
- Use comments to mark logical phases or explain non-obvious intent.  Separate
  a full-line comment block from preceding code with one blank line.
- Prefer Click for command-line interfaces.
- Tests should be focused, readable and cover important behavior.
- Always run Pylint on modified Python code.  Suppress warnings only with a
  nearby explanation.

## Validation

Run the test suite after changing the installer or canonical sources:

```sh
pytest tests
```

Run Pylint on modified Python code:

```sh
pylint scripts/install tests
```

Validate modified TOML and JSON files, ensure generated native subagent files
parse successfully and check Markdown files for obvious formatting problems.
