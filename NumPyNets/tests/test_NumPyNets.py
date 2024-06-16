"""
Unit and regression test for the NumPyNets package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import NumPyNets


def test_NumPyNets_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "NumPyNets" in sys.modules
