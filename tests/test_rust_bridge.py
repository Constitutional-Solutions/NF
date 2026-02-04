import unittest
from unittest.mock import patch

from genesis_kernel.rust_bridge import load_legion_core_rs, rust_status
from genesis_kernel.quantum import QuantumHarmonicEngine
from genesis_kernel.constants import UniversalConstants
from genesis_kernel.love_math import LoveMathematics
from genesis_kernel.pattern_math import quadratic_growth_stream


class RustBridgeTests(unittest.TestCase):
    def test_rust_status_matches_loader(self) -> None:
        module = load_legion_core_rs()
        status = rust_status()
        if module is None:
            self.assertFalse(status["available"])
        else:
            self.assertTrue(status["available"])
        self.assertEqual(status["module"], "legion_core_rs")

    def test_quantum_fallback_when_rust_missing(self) -> None:
        with patch("genesis_kernel.quantum.load_legion_core_rs", return_value=None):
            constants = UniversalConstants()
            love = LoveMathematics(constants)
            engine = QuantumHarmonicEngine(constants, love)
            result = engine.energy_eigenvalue(2)
            self.assertGreater(result, 0)

    def test_pattern_fallback_when_rust_missing(self) -> None:
        with patch("genesis_kernel.pattern_math.load_legion_core_rs", return_value=None):
            trace = quadratic_growth_stream(2.0)
            self.assertEqual(trace[-1], 9.0)

    def test_quantum_partial_failure_falls_back(self) -> None:
        class FailingEngine:
            def energy_eigenvalue(self, *_args, **_kwargs):
                raise RuntimeError("boom")

            def phi_quantization(self):
                raise RuntimeError("boom")

        class FakeModule:
            QuantumEngineRS = FailingEngine

        with patch("genesis_kernel.quantum.load_legion_core_rs", return_value=FakeModule()):
            constants = UniversalConstants()
            love = LoveMathematics(constants)
            engine = QuantumHarmonicEngine(constants, love)
            value = engine.energy_eigenvalue(1)
            self.assertGreater(value, 0)
            glyph = engine.phi_quantization()
            self.assertIn("phi_base", glyph)

    def test_pattern_partial_failure_falls_back(self) -> None:
        class FailingPattern:
            @staticmethod
            def quadratic_growth_stream(_input):
                raise RuntimeError("boom")

        class FakeModule:
            PatternEngineRS = FailingPattern

        with patch(
            "genesis_kernel.pattern_math.load_legion_core_rs",
            return_value=FakeModule(),
        ):
            trace = quadratic_growth_stream(2.0)
            self.assertEqual(trace[-1], 9.0)


if __name__ == "__main__":
    unittest.main()
