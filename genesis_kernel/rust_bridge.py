"""Rust acceleration bridge for optional legion_core_rs bindings."""
from __future__ import annotations

import os
from importlib import import_module, util
from typing import Optional


def load_legion_core_rs() -> Optional[object]:
    """Return the legion_core_rs module if available, otherwise None."""
    if os.getenv("LEGION_FORCE_PYTHON") == "1":
        return None
    spec = util.find_spec("legion_core_rs")
    if spec is None:
        return None
    return import_module("legion_core_rs")


def rust_status() -> dict[str, str | bool]:
    """Return a summary of Rust acceleration availability."""
    module = load_legion_core_rs()
    return {
        "available": module is not None,
        "module": "legion_core_rs",
    }
