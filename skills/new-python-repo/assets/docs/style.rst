Coding Style Conventions
========================

This guide defines the Python coding conventions used throughout the project.
Follow `PEP 8 <https://peps.python.org/pep-0008/>`_ where this guide does not
specify otherwise.

Readability, Names and Encapsulation
------------------------------------

Use ``snake_case`` for variables at every scope, including module globals and
constants.  Use ``CamelCase`` for classes and enums.  This deliberately differs
from PEP 8's all-caps convention for constants.

Prefer descriptive names, allowing conventional short names when their
meaning is clear in context.  Examples include mathematical symbols and
indices, ``ex`` for exceptions, ``fh`` or ``fp`` for file handles, ``ax`` or
``fig`` for plotting objects and ``src`` or ``dst`` for source and destination.

Mathematical variable names are appropriate when their meaning is clear from
the surrounding context, such as ``y = z * x``.

Use a leading underscore for module-private classes and for attributes whose
names or behavior may change.  It is guidance to callers rather than strict
information hiding.  Leave stable, useful names public when doing so does not
needlessly constrain future implementation choices.

Use comprehensions for plainly readable collection construction.  Prefer an
ordinary loop when nesting, branching or intermediate reasoning would make a
comprehension difficult to follow.

Prefer::

    squares = [value**2 for value in values]

Prefer a loop when it exposes the structure of the work::

    coordinates = []
    for row_index, row in enumerate(array):
        for column_index, value in enumerate(row):
            if value > threshold:
                coordinates.append((row_index, column_index))

Choose the clearest control flow for the context.  An implicit ``None`` return
and a short conditional expression are both acceptable when they are obvious.
Do not adopt rigid rules about early returns or conditional expressions.

Type Annotations
----------------

Do not add type annotations unless they support an actual integration or
workflow.  Otherwise, document useful type information in docstrings.

Docstrings
----------

Public and private modules, classes, functions and methods must have
docstrings.  A concise docstring is sufficient for a simple private helper.
An overriding method may inherit its documentation when the inherited
docstring remains accurate.

Use the following Google-inspired docstring format.  It supports
reStructuredText formatting, keeps prose at 80 characters and places each
argument description below its name and type.  Order sections as ``Args``,
``Returns`` or ``Yields``, ``Raises``, ``Notes`` and ``References``, omitting
sections that do not apply.  References may use a name and link or BibTeX.

Use double quotes, begin the text immediately after the opening quotes and
place closing docstring quotes on a separate line.  Use reStructuredText
markup where it improves clarity.

.. code-block:: python

    class ValueCalculator:
        """Calculate values using a fixed offset and divisor.
        """

        def __init__(self, offset, divisor=42):
            """Initialize the calculator.

            Args:
                offset (int | float):
                    The offset added to each input value.
                divisor (int | float):
                    The nonzero divisor applied after adding ``offset``.
            """
            self.offset = offset
            self.divisor = divisor

        def calculate(self, value):
            """Compute ``(value + offset) / divisor``.

            Args:
                value (int | float):
                    The input value.

            Returns:
                (float):
                    The result of the calculation.

            Raises:
                ZeroDivisionError:
                    If ``divisor`` is zero.

            Notes:
                The result is a ``float`` even when the inputs are integers.
            """
            return (value + self.offset) / self.divisor

        def reset(self):
            """Reset ``offset`` to zero.
            """
            self.offset = 0

Comments
--------

Use comments liberally when they explain intent or non-obvious behavior.  Begin
comments with a capital letter.  A single-sentence comment has no ending period.
Multi-sentence or multi-line comments use ending periods and two spaces after
each period.

Separate full-line comments from preceding code with exactly one blank line.
Keep consecutive comments that form one logical block together without blank
lines between them.

Prefer::

    # This is a single line comment

    # This comment has multiple sentences.  Use a period and two spaces.

    # This is a very long comment.  It explains something in depth and
    # has multiple lines and multiple sentences.  We use periods here too.

Inline Code in Comments and Messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Comments, log messages and exception messages are not rendered as RST.  Use
single backticks to distinguish code from natural language in these contexts.

Prefer::

    # Apply `offset` before dividing
    result = (value + offset) / divisor

Prefer::

    raise ValueError(f'Invalid `{method=}`.')

Imports
-------

Group imports into standard library, third-party and local sections, separated
by one blank line.  Keep imports alphabetized within each section, and do not
use wildcard imports.

Keep library namespaces in code to show where names originate and to prevent
name collisions.  Avoid importing functions and classes directly, except when
re-exporting a package's public interface, such as in ``__init__.py``.

Some packages do not load submodules when their top-level package is imported.
Import the submodule as ``_`` when needed to access it through the parent
namespace.

Prefer::

    import scipy as sp
    import scipy.optimize as _

    result = sp.optimize.minimize(objective, initial_guess)

Acceptable::

    from scipy import optimize

Avoid::

    from scipy.optimize import LinearConstraint

Use this pattern only to load a submodule for access through its parent
namespace, rather than merely to silence an unused-import warning.

Use these aliases consistently::

    import numpy as np
    import torch as th

Prefer ``pathlib`` for local filesystem paths.

Formatting
----------

Line Length and Whitespace
~~~~~~~~~~~~~~~~~~~~~~~~~~

Soft-wrap Python code near 90 characters where there is a natural breakpoint.
Do not exceed 100 characters unless a URL or another unbreakable string makes
that necessary.  Pylint permits 101 characters to allow this judgment.
Docstrings and documentation prose wrap at 80 characters.  Code examples in
documentation follow the Python code limits.

Use one blank line between top-level definitions, methods and logical
sections of code.  Do not use double blank lines in Python.

Strings
~~~~~~~

Prefer single-quoted strings, except in docstrings.  Double quotes are
appropriate when they improve readability, such as when a string contains
an apostrophe.

Prefer f-strings for interpolation::

    message = f'Calculated {count} values.'

Acceptable::

    message = "The calculation isn't finished."

Dictionaries and Lists
~~~~~~~~~~~~~~~~~~~~~~

Place closing brackets on their own line in long dictionaries and lists.
Use trailing commas to make adding items easier.

Prefer::

    results = {
        'mean': mean,
        'variance': variance,
    }

    values = [
        first_value,
        second_value,
    ]

Function and Method Signatures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A long function or method signature wraps horizontally rather than placing
one argument on every line.

Prefer::

    def function_signature(arg1, arg2, min_value=0., max_value=10.,
                           tolerance=32., method='iterative'):
        """Demonstrate a compact function signature.
        """

Function Calls
~~~~~~~~~~~~~~

Keep short calls on one line.  For calls with several arguments, prefer
keywords when they clarify the argument's meaning or avoid reliance on order.
Short, obvious positional arguments remain appropriate.

Prefer::

    function(x, y, min_value=0., max_value=10.)

Arguments may begin on the line after the opening parenthesis.  Place the
closing parenthesis on its own line when that improves readability, and use
a trailing comma when doing so.

Acceptable::

    long_function_name(
        x, y, min_value=0., max_value=10.)

    long_function_name(
        x, y, min_value=0., max_value=10.,
    )

    function(
        x, y,
        min_value=0.,
        max_value=10.,
    )

Keep nested calls readable by giving their closing parentheses separate lines
when wrapping across multiple lines.

Prefer::

    process_images(
        load_images(
            image_dir, filenames, transform=transform,
        ),
    )

Avoid::

    process_images(
        load_images(
            image_dir, filenames,
            transform=transform))

Documentation Prose
-------------------

Write Sphinx documentation under ``docs/`` in reStructuredText.  Other
repository documentation may use Markdown.  Wrap prose at 80 characters.  Use
title case for headings, two spaces after sentence-ending periods and no Oxford
commas.  Follow existing documentation patterns for Sphinx page structure and
cross-references.
