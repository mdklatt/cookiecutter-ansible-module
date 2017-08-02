""" Test suite for the {{ cookiecutter.module_name }} module.

The script can be executed on its own or incorporated into a larger test suite.
The ANSIBLE_LIBRARY environment variable must include src/, and pytest must be
run with `--ansible-host-pattern=localhost`.

"""
import pytest


@pytest.mark.xfail(reason="not implemented")
def test_{{ cookiecutter.module_name }}():
    """ Test the {{ cookiecutter.module_name }} module.
    
    """
    assert False
    return


# Make the module executable.

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
