from types import ModuleType
from tf_lazy_loader import dynamic_import, _LazyLoader

def test_runs():
    os = dynamic_import("os", lazy=False)
    assert os is not None

def test_runs_lazy():
    os = dynamic_import("os")
    assert isinstance(os, _LazyLoader)
