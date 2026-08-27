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
