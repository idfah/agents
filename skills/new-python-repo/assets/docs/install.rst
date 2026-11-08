Installation
============

The minimum supported Python version is {{python_version}}.

From the repository root, create and activate a virtual environment:

.. code-block:: console

   python3 -m venv venv
   source venv/bin/activate

Use an interpreter that satisfies the project's Python requirement.
Install the package in editable mode so source changes are available without
reinstalling:

.. code-block:: console

   python -m pip install -e .

For development, include the lint, test, packaging and documentation tools:

.. code-block:: console

   python -m pip install -e '.[dev]'

Continue with :doc:`develop` for the development commands.
