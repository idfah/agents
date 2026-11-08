Development
===========

Follow :doc:`install` to install the package with development dependencies.
Run commands from the repository root with your environment activated.
Make uses ``python`` from your current environment.

Checks
------

Run lint on the package, tests and Sphinx configuration:

.. code-block:: console

   make lint

Run tests, with lint as a prerequisite:

.. code-block:: console

   make test

The initial smoke test checks package imports.  See :doc:`style` for coding
conventions.

Documentation
-------------

Build the Sphinx HTML pages, treating warnings as failures:

.. code-block:: console

   make docs

Open ``docs/_build/html/index.html`` to browse the output.  For a fresh build:

.. code-block:: console

   make docs-clean && make docs

``make docs-clean`` removes generated documentation under ``docs/_build/``.

Packaging
---------

Build a wheel after lint and tests pass:

.. code-block:: console

   make wheel

The wheel is written to ``dist/``.  Build output is ignored by Git.

Repository Layout
-----------------

``{{package_name}}/`` contains the Python source.  ``tests/`` holds tests and
``scripts/`` holds supplemental development scripts.  ``context/`` is for
temporary, uncommitted drafts and findings rather than historical records.
