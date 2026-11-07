Coding Style Conventions
========================

This guide supplements `PEP 8 <https://peps.python.org/pep-0008/>`_.  Follow
PEP 8 and established Python practice for conventions not addressed here.
This guide is the source of truth for style and coding conventions in this
repository.  The ``.pylintrc`` file enforces the subset that Pylint can check.

Line Length and Whitespace
--------------------------

Soft-wrap Python code near 90 characters where there is a natural breakpoint.
Do not exceed 100 characters unless a URL or another unbreakable string makes
that necessary.  Pylint permits 101 characters to allow this judgment.
Docstrings and documentation prose wrap at 80 characters.

Do not use double blank lines in Python.  Use single-quoted strings.

Calls and Signatures
--------------------

Keep short calls on one line.  For calls with several arguments, prefer
keywords when they clarify the argument's meaning or avoid reliance on order.
Short, obvious positional arguments remain appropriate.

Prefer::

    function(x, y, min_value=0., max_value=10.)

Acceptable::

    long_function_name(
        x, y, min_value=0., max_value=10.)

    function(
        x, y,
        min_value=0.,
        max_value=10.,
    )

Avoid::

    long_function_name(
        x, y, min_value=0., max_value=10.,
    )

Use trailing commas in wrapped calls.  A long function or method signature
wraps horizontally rather than placing one argument on every line.

Prefer::

    def function_signature(arg1, arg2, min_value=0., max_value=10.,
                           tolerance=32., method='iterative'):

Names, Imports and Encapsulation
--------------------------------

Use ``snake_case`` for variables at every scope, including module globals and
constants.  Use ``CamelCase`` for classes and enums.  This deliberately differs
from PEP 8's all-caps convention for constants.

Use a leading underscore for module-private classes and for attributes whose
names or behavior may change.  It is guidance to callers rather than strict
information hiding.  Leave stable, useful names public when doing so does not
needlessly constrain future implementation choices.

Keep library namespaces in code to show where names originate and to prevent
name collisions.

Prefer::

    import scipy as sp
    import scipy.optimize as _

Acceptable::

    from scipy import optimize

Avoid::

    from scipy.optimize import LinearConstraint

Bind an intentionally loaded submodule to ``_`` only when it must be available
through its parent namespace, such as ``sp.optimize``.  It is not a general way
to silence unused imports.

Types and Readability
---------------------

Do not add type hints by default.  Use them when they provide a concrete
benefit, such as defining a framework-facing tool interface.  Otherwise,
document useful type information in a docstring.

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

Docstrings and Comments
-----------------------

Use the following Google-inspired docstring format.  It supports
reStructuredText formatting, keeps prose at 80 characters and places each
argument description below its name and type.  ``Notes`` and ``References``
are optional sections.

.. code-block:: python

    def method_or_function_signature(self, value1, value2, method='fixed'):
        """A method that does something interesting and is explained here.  Our
        docs are Sphinx RST, so we can use RST formatting.  Keep docstrings
        wrapped at 80 characters.

        Notes:
            Optional section with important notes to flag.  May be a bulleted
            list.

        References:
            References are optional and can be informative, including a URL
            link or a BibTeX reference.

        Args:
            value1 (int):
                The first value is used for this.
            value2 (None | float):
                The second value is optional and is used for something else.
            method (str):
                This describes the method to use.

        Returns:
            (dict[str, float]):
                The return value maps strings to floating point values.
        """

Use comments liberally when they explain intent or non-obvious behavior.  Do
not comment on obvious code.  Begin comments with a capital letter.  A
single-sentence comment has no ending period.  Multi-sentence or multi-line
comments use ending periods and two spaces after each period.

Prefer::

    # This is a single line comment

    # This comment has multiple sentences.  Use a period and two spaces.

    # This is a very long comment.  It explains something in depth and
    # has multiple lines and multiple sentences.  We use periods here too.

Documentation Prose
-------------------

Write documentation in reStructuredText.  Wrap prose at 80 characters.  Use
sentence case, two spaces after sentence-ending periods and no Oxford commas.
Follow existing documentation patterns for Sphinx page structure and
cross-references.
