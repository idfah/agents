"""Smoke tests for the package.
"""
import importlib

def test_imports():
    """Verify that the package is importable.
    """
    modules = ['{{package_name}}']

    for module in modules:
        importlib.import_module(module)
