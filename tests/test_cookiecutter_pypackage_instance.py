"""Tests concerning the `cookiecutter_pypackage_instance` module."""

from cookiecutter_pypackage_instance.cookiecutter_pypackage_instance import factorial


def test_cookiecutter_pypackage_instance():
    assert factorial(5) == 120
