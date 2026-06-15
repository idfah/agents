# Overview

This file defines my personal style, preferences and best-practices for
software development.

When writing code, prioritize consistency, readability, maintainability, and
adherence to these conventions except when overridden by repo-level
conventions or configuration.

# About me

- I am a highly skilled programmer.
- I am a machine learning scientist with a PhD in computer science.
- I specialize in building machine learning systems for satellite imagery.

# Global Rules

- Do not make any changes unless explicitly instructed to do so.
- Prefer clear, readable, maintainable code.
- Avoid surprising behavior from the caller's perspective.
- Avoid over engineering, excessive error handling and excessive validation.
- Prefer allowing errors to arise naturally over explicit checks, unless adding
  an explicit check improves debugging clarity or avoids surprising behavior.
- Prefer readable, descriptive variable and method names.
- Prefer code that is organized and easy to understand.
- All classes, methods, and functions must have docstrings.
- Private methods must also have docstrings; although they can be abbreviated.
- Match the style and structure already present in the codebase.
- Project-specific instructions override this global file when they conflict.
- Always state ambiguities and potential sources of issues when planning.
- Stop and ask before making large changes that were not discussed in the
  design, plan or prompt.

# Python Style

- Follow PEP 8 style unless a rule below explicitly overrides it.
- Do not use type hints in code.
- Use consistent, readable formatting.
- Prefer descriptive names over short names, except for conventional short
  names in small local contexts.
- Avoid unnecessarily dense expressions when they reduce readability.
- Prefer straightforward control flow unless a more concise form is equally
  readable.
- Do not use double blank lines anywhere.
- Use named keyword arguments when a function call has more than two
  arguments.

## Line Length

- Target a soft line length of 90 characters.
- Hard maximum line length is 100 characters.
- Wrap lines as needed to stay within these limits.
- Docstrings should wrap between 80-90 characters.

## String Style

- Prefer single quotes for all strings.
- Use double quotes only for docstrings.

Example:

    value = 'example string'

    def function():
        """This is a docstring that uses double quotes.
        """
        return 'result'

## Imports

- Group imports into three sections:
  1. Standard library
  2. Third-party libraries
  3. Local/project imports
- Separate each section with a single blank line.
- Keep imports in alphabetical order within each section.
- Do not use wildcard imports.

## Import Style

- Prefer namespace imports over importing individual components.
- Namespaces improve readability and make it clear where symbols originate.
- Namespaces also help prevent name collisions.

Preferred pattern:

    import skimage as ski
    import skimage.io as _

Usage:

    img = ski.io.read(filename)

- Do not import functions or classes directly unless there is a strong
  justification.
- Avoid patterns like:

    from skimage.io import imread

- Prefer:

    import skimage as ski

- The alias `_` may be used for submodules when they are only imported to
  register access through a parent namespace.

## Preferred Aliases

Use these aliases consistently:

    import lightning
    import matplotlib.pyplot as plt
    import numpy as np
    import rasterio as rio
    import scipy as sp
    import shapely as shp
    import skimage as ski
    import torch as th
    import torchmetrics as tm

- Prefer `pathlib` for filesystem path handling.
- Prefer `fsspec` in order to support remote files.

## Comments

- Use comments liberally where they improve readability or explain intent.
- Keep comments concise but use use clear, complete sentences.
- Comments that span multiple lines or contain multiple sentences end with
  a period.
- Single-line comments containing a single-sentence do not end with a period
- Full-line comments should be visually separated from preceding code by exactly
  one blank line.
- Consecutive full-line comments that form one logical block should stay
  together with no blank lines between them.

Single-line comment style:

    # This is a single-line comment

Multi-line or multi-sentence comment style:

    # This is a longer comment. It has periods because
    # it is multiple lines or multiple sentences.

- Prefer comments that describe why rather than what, unless the what is
  not obvious.
- Do not add redundant or trivial comments.

## Docstrings

- Use Google-style docstrings.
- Every class, function, method, and private method must have a docstring.
- For public functions and methods, document arguments and return values
  when applicable.
- Each argument must be documented on its own line, with the description
  indented on the following line.

Example:

    def function(arg1, arg2, arg3):
        """This is my method. It does something interesting.

        Args:
            arg1 (int):
                This argument does something.
            arg2 (list[int]):
                This argument does something else.

        Returns (str):
            This function returns a string describing something.
        """

- Private method docstrings may be abbreviated and do not need argument
  documentation when the intent is clear.

# Design Preferences

- Prefer object-oriented design unless it clearly does not make sense.
- Use classes when they improve structure, clarity, or encapsulation.
- Do not force object-oriented design when a simple function is better.
- Prefer designs that are easy to extend and maintain.
- Prefer clean integration and interface boundaries that are clear to new users.
- Favor separation of responsibilities.
- Use @staticmethod when appropriate.
- Use @classmethod for additional initializer methods.

# Preferred Libraries

- Prefer: NumPy, SciPy, PyTorch, Rasterio, Scikit-Image, Fiona, Shapely,
  Matplotlib, Lightning, TorchMetrics, TensorBoard, WandB, TorchVision,
  pathlib, click
- Prefer these over alternatives unless there is a strong reason not to.
- Do not introduce new dependencies unnecessarily.

# Testing

- Unit tests should be simple and human-readable.
- Follow the general style, conventions and spirit of the existing tests.
- Prioritize integration testing, happy-path tests and likely edge cases.
- Ensure core functionality and major edge-cases are verified but full test
  coverage is not required.
- Use names like mock, `_mock` and `_Mock` for stub / mock classes and
  functions.
- Prefer names like `foo`, `bar`, `baz` and `boo` for artificial, nonsense
  string arguments.
- Always run pylint.
- Unit tests may disable pylint warnings where appropriate.
- Stop and ask before disabling pylint warning or working around pylint
  warnings in core code.

# PyTorch Conventions

- Prefer defining custom torch.nn.Module subclasses over factory functions.
- Encapsulate behavior inside modules.
- Prefer subclassing existing modules over wrapping them.
- Use Kaiming uniform weight initialization unless instructed otherwise.

Example:

    class _Linear(th.nn.Linear):
        """A Linear layer with Kaiming weight initialization.
        """
        def reset_parameters(self):
            """Reset or initialize parameters.
            """
            th.nn.init.kaiming_uniform_(self.weight, nonlinearity='linear')
            if self.bias is not None:
                th.nn.init.zeros_(self.bias)

Avoid:

    def make_linear(**kwargs):
        linear = th.nn.Linear(**kwargs)
        th.nn.init.kaiming_uniform_(linear.weight, nonlinearity='linear')
        if linear.bias is not None:
            th.nn.init.zeros_(linear.bias)
        return linear

# Output Expectations

- Produce complete, runnable code.
- Preserve existing style when modifying code.
- Keep explanations concise unless asked otherwise.

## Status emoji legend

When generating responses, use these emoji as status markers:

- ✅ Done / correct / recommended
- ⚠️ Warning / caveat / risk
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
- Only use emoji in responses.
- Do not use emoji in code, diffs, logs, filenames, identifiers, config files,
  tests, comments, commit messages, or other machine-readable/generated
  artifacts unless explicitly requested.
- Emoji are for explanatory prose, headings, summaries, and bullet labels only.
