# Agent Configurations

This repository contains the source configuration for my coding assistants and
agentic workflows.  It supports Codex, Claude and Copilot CLI while keeping
shared skills and subagent instructions in one place.

## Structure

```text
codex/       Codex instructions and baseline configuration
claude/      Claude instructions and baseline configuration
copilot/     Copilot instructions and baseline configuration
skills/      Shared skills with co-located native metadata
subagents/   Shared subagent roles with tool-specific settings
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
scripts/install copilot
```

The installer writes to `~/.codex`, `~/.claude` or `~/.copilot`.  It overwrites
managed instructions, same-named skills and same-named subagents while leaving
unrelated local files untouched.  Existing `config.toml` and `settings.json`
files are preserved unless `--force` is used.

Use `--dry-run` to preview an installation without making changes.  Use
`--force` to replace every managed file, including the main configuration:

```sh
scripts/install --dry-run codex
scripts/install --force claude
```

## Copilot CLI

Copilot installs personal instructions, shared skills and native `.agent.md`
subagent files.  Each subagent specifies its model and reasoning effort; both
are refreshed on installation.  Project `AGENTS.md` files provide local
guidance.

The settings baseline enables assisted approvals, sandboxing and memory.
Assisted approvals reduce prompts but do not guarantee human approval for every
risky action.  The generic sandbox permits development-tool access beyond the
repository; review the effective policy with `/sandbox policy`.  Review agents
omit editing tools, but shell access still relies on their read-only
instructions.

Mouse capture, startup tips and banners are disabled.  Copilot uses its normal
alternate-screen interface, which can limit tmux scrollback; there is no
documented independent switch to disable it.  Screen-reader mode is left
disabled.

Press Ctrl+G to edit a prompt in an external editor.  Copilot selects the
editor from `COPILOT_EDITOR`, `VISUAL` or `EDITOR`, in that order.  For Vim,
launch with
`COPILOT_EDITOR=vim copilot`.  Composer bindings remain at their defaults.
