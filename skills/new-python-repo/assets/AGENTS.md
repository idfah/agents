# Purpose

{{description}}

# Repository Layout

```text
{{package_name}}/  Python package
docs/             Installation, development workflow and coding style
tests/            PyTest tests
scripts/          Supplemental development scripts
context/          Temporary, uncommitted working documents
```

Read relevant documentation before implementing changes.
`docs/style.rst` is authoritative for coding conventions.  Consult it when
beginning work, when it changes or when a convention is unclear.

# Development

Prefer simple, readable code, clear interfaces and few special cases.

- Keep `context/` for current drafts and findings, not a historical archive.
- Run `make test` for Python changes; lint must pass before tests run.
- Run `make docs` for Sphinx changes; documentation warnings fail the build.
- Ask before disabling or loosening lint rules, including in tests, or
  restructuring code merely to work around an unhelpful lint restriction.
