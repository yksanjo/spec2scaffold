import importlib


def test_main_exists():
    mod = importlib.import_module("spec2scaffold.cli")
    assert hasattr(mod, "main")
