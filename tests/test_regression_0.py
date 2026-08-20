import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)


def test_regression_0():
 """Regression guard for a render edge case discovered earlier."""
 from schemadiff.features.feature-render-0 import run_render
 result = run_render("sample-0", timeout=5)
 assert result["ok"] is True
 assert "value" in result