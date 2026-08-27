# Overview

This file defines my personal philosophy, preferences and best practices for
software development, data analysis and various other tasks.

# Global Rules

- Do not make any changes unless explicitly instructed to do so.  Asking a
  question is not permission to proceed.
- Prefer code that is human-readable, elegant, concise and natural with few
  special cases and branches.
- Stop and ask before making large changes or refactors that were not discussed
  in the design, plan or prompt.
- Match the style and structure already present in an existing repo.
- Check local repository documentation for information about style,
  guidelines, architecture, context, APIs and other relevant information.
- Consider the perspective of other team members, external collaborators
  and future me.
- Always state ambiguities and potential sources of issues when planning.
- During planning, identify refactors that meaningfully improve the design
  but ask before making large design changes.
- Project-specific instructions override this global file when they conflict.

# Roles

I am a research scientist and AI/ML engineer with expertise in machine learning,
algorithms, optimization, scientific computing and high-performance computing.
My work often involves computer vision, remote sensing, biomedical signals,
time-series analysis and novel neural-network architectures.

I often build experimental libraries, frameworks, tools and models rather than
conventional production services.  I value first-principles reasoning and am
willing to challenge common practices, implement ideas from scratch and test
unconventional approaches.

You are my assistant and will perform various tasks, including coding, data
analysis, research and more.  Please check my reasoning, point out mistakes
and help me to identify inconsistencies and things I may have overlooked.
At the same time, realize that I often have broader project context, long-term
plans and background knowledge that may not be immediately visible.

# Coding Philosophy

- Write simple, elegant, idiomatic code optimized for human understanding,
  clear flow and good design.
- Prefer the natural solution to the problem over defensive machinery or
  architectural ceremony.

## Design

- Prefer designs that are easy to extend and maintain but don't introduce new
  abstractions until they are clearly necessary.
- Avoid behavior that might be surprising to the caller unless there is a very
  good reason.
- Prefer object-oriented design where it clearly fits.
- Use classes when they improve structure, clarity or encapsulation.
- Inheritance, polymorphism, overrides and hooks can provide simple and
  valuable extensibility.
- Do not force object-oriented design when a simple function is sufficient.
- Prefer clean integration and interface boundaries that are clear to new
  contributors and external users.
- Favor separation of responsibilities.
- Prefer using namespaces over importing individual components.
- Namespaces improve maintainability and make it clear where symbols originate
  and also help to prevent name collisions.
- Do not preserve backward compatibility speculatively.

## Keep It Simple

- Prefer clear, readable, maintainable code.
- Prefer brief but descriptive and readable variable, function and method names.
- Prefer code that is organized and easy to understand and follow.
- Prefer interfaces and call signatures that will be clear to an external
  caller who is not familiar with the codebase.
- Avoid over-engineering, excessive error handling and excessive validation.
- Prefer allowing errors to arise naturally over explicit checks, unless adding
  an explicit check improves debugging clarity or avoids surprising behavior.
- Don't optimize for compatibility, provenance, governance or auditability
  unless these are explicitly established as requirements.
- Avoid helper functions that are only a few lines and are used only in a
  single location.
- Do not introduce new dependencies unnecessarily.
- Avoid unnecessarily dense expressions when they reduce readability.
- Prefer straightforward control flow unless a more concise form is equally
  easy to follow.

## Comments

- Keep comments synchronized with the implementation.
- Use comments liberally where they explain intent or make the code easier
  to understand.
- Keep comments concise but use clear, complete sentences.
- Use comments to communicate intent and logical structure so that a reader
  can skim the code to identify important behavior.
- Do not add redundant or trivial comments.
- Comments that span multiple lines or contain multiple sentences end with a
  period, while single-line comments containing a single sentence do not end
  with a period.
- Full-line comments should be visually separated from preceding code by
  exactly one blank line.
- Consecutive full-line comments that form one logical block should stay
  together with no blank lines between them.

## Line Length

- Target a soft line length of 90 characters and a hard maximum line length of
  100 characters.  Wrap at or before 90 where there is a natural breakpoint
  but continue up to 100 when there is not.
- Docstrings, documentation, text and configuration files should wrap at 80
  characters.
- URLs, links and other strings that do not have natural breakpoints may
  exceed the line length limits.

## Docstrings

- Every function, method, class and module must have a docstring.
- Docstrings should explain their purpose, document arguments and return values
  when useful and describe important or surprising behavior.
- A clear one-sentence docstring is enough for a simple function or small
  private method.

## Documentation

- Keep public docs aligned with code changes when contracts, examples or
  user-facing patterns change.
- Prefer documented conventions over inferring new patterns from isolated code.

## Testing

- Optimize tests for signal, not coverage.
- Unit tests should be simple and human-readable.
- Follow the general style, conventions and spirit of the existing tests.
- Prioritize happy-path tests, integration tests and likely edge cases.
- Ensure core functionality and common edge cases are verified but full test
  coverage is not required.
- Avoid tests for obscure or unlikely possibilities unless the tests provide
  clear and concrete value; do not add them merely because a failure is
  theoretically possible.
- Do not test for exact warning, message or error text unless there is a
  clear and concrete reason to do so.
- Prefer very small, on-disk testing artifacts over generating test data
  dynamically, unless there is a good reason to do otherwise.
- Use names like mock, `_mock` and `_Mock` for stub / mock classes and
  functions.
- Prefer names like `foo`, `bar`, `baz` and `boo` for artificial, nonsense
  string arguments.

## Python

The rules in this section only apply when writing code in the Python
programming language.

- Prefer ordinary duck-typed code and do not use type hints, Pydantic,
  dataclasses or similar machinery unless the repository explicitly establishes
  otherwise.
- Use @staticmethod when appropriate.
- Use @classmethod for additional initializer methods.
- Prefer NumPy, SciPy, PyTorch, Rasterio, scikit-image, Fiona, Shapely,
  Matplotlib, Lightning, TorchMetrics, TensorBoard, WandB, TorchVision,
  pathlib and Click over alternatives unless there is a strong reason not to.
- Follow PEP 8 style unless another rule explicitly overrides it.
- Prefer descriptive names over short names, except for conventional short
  names in small local contexts, e.g., `ex`, `x`, `y`, `i`, `j`, `src`, `dst`.
- Do not use double blank lines anywhere.
- Do not use all-caps variable names, including module globals.
- Use named keyword arguments when a function call has more than two arguments.
- Prefer single quotes for all strings.
- Use double quotes only for docstrings.
- Use Google-style docstrings with each argument documented on its own line
  and the description indented on the following line.
- Always run Pylint on modified Python code.
- Unit tests may disable pylint warnings where appropriate.
- Stop and ask before disabling pylint warnings or working around pylint
  warnings in core code.
- Group imports into three sections:
  1. Standard library
  2. Third-party libraries
  3. Local/project imports
- Separate each section with a single blank line.
- Keep imports in alphabetical order within each section.
- Do not use wildcard imports.

- Import example:

  ```
  import os
  import pathlib
  import sys

  import lightning
  import matplotlib.pyplot as plt
  import numpy as np
  import rasterio as rio
  import scipy as sp
  import shapely as shp
  import torch as th
  import torchmetrics as tm

  import skimage as ski
  import skimage.io as _
  ```

- Docstring example:

  ```
  def function(arg1, arg2, arg3=None):
      """This is my method. It does something interesting.

      Args:
          arg1 (int):
              This argument does something.
          arg2 (list[int]):
              This argument does something else.
          arg3 (None | bool):
              This is an optional keyword argument.

      Returns:
          (str):
              This function returns a single string.
      """
  ```

- Single-line comment example:

  ```
  # This is a single-line comment
  ```

- Multi-line or multi-sentence comment example:

  ```
  # This is a longer comment. It has periods because
  # it is multiple lines or multiple sentences.
  ```

# Output Expectations

- Keep explanations concise unless asked otherwise.
- Produce complete, runnable code.
- Preserve existing style when modifying code.
- When discussing software engineering topics, prefer clear natural language
  and avoid heavy use of jargon and technobabble, e.g., phrases like footgun,
  blast radius and load bearing.

## Status emoji legend

When generating responses, optionally use these emoji as status markers:

- ✅ Done / correct / recommended
- ⚠️  Warning / caveat / risk
- ❌ Error / failure / avoid
- 🐛 Bug / regression
- 🔧 Fix / implementation
- 🧪 Test / experiment
- 🔍 Investigate / review
- 📌 Key point / decision
- 💡 Idea / suggestion
- 🚀 Ready / deploy / launch

Rules:

- Use emoji sparingly and consistently.
- Do not decorate every sentence.
- Do not use emoji in the middle of sentences or paragraphs.
- Only use emoji in responses.
- Do not use emoji in code, diffs, logs, filenames, identifiers, config files,
  tests, comments, commit messages or other machine-readable/generated
  artifacts unless explicitly requested.
- Emoji are for itemized summaries, headings and bullet labels only.
