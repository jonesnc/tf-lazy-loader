import pytest
import importlib

from tf_lazy_loader import _LazyLoader, dynamic_import


def test_runs():
    """Test that calling dynamic_import(..., lazy=False) still returns module."""
    os = dynamic_import("os", lazy=False)
    assert os is not None


def test_runs_lazy():
    """Test that calling dynamic_import returns a _LazyLoader instance."""
    os = dynamic_import("os")
    assert isinstance(os, _LazyLoader)


def test_lazily_loaded_is_set():
    """Test that _ll_lazily_loaded is set to True by dynamic_import(..., lazy=True)."""
    os = dynamic_import("os")
    assert os._ll_lazily_loaded is True
