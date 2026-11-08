.PHONY: test lint docs docs-clean wheel

lint:
	python -m pylint {{package_name}} tests docs/conf.py

test: lint
	python -m pytest

docs:
	python -m sphinx -b html -W docs docs/_build/html

docs-clean:
	rm -rf docs/_build

wheel: test
	python -m build --wheel
