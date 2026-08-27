# Agent Configurations

This repository contains the source configuration for my coding assistants and
agentic workflows.  It currently supports Codex and Claude while keeping shared
skills and subagent instructions in one place.

## Structure

```text
codex/       Codex instructions and baseline configuration
claude/      Claude instructions and baseline configuration
skills/      Shared skills with co-located native metadata
subagents/   Shared subagent roles with Claude and Codex settings
scripts/     Installation script
tests/       Installer tests
```

## Installation

Use Python 3.11 or newer and install the unpinned dependencies:

```sh
pip3 install -r requirements.txt
```

Then install the configurations for one tool at a time:

```sh
scripts/install codex
scripts/install claude
```

The installer writes to `~/.codex` or `~/.claude`.  It overwrites managed
instructions, same-named skills and same-named subagents while leaving unrelated
local files untouched.  Existing `config.toml` and `settings.json` files are
preserved unless `--force` is used.

Use `--dry-run` to preview an installation without making changes.  Use
`--force` to replace every managed file, including the main configuration:

```sh
scripts/install --dry-run codex
scripts/install --force claude
```
