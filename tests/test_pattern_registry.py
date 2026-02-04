import unittest

from genesis_kernel.pattern_math import (
    PatternMetadata,
    PatternRegistry,
    PatternTransformation,
)


class PatternRegistryTests(unittest.TestCase):
    def test_register_metadata_snapshot(self) -> None:
        registry = PatternRegistry()
        pattern = PatternTransformation(name="test", steps=["a", "b"])
        metadata = PatternMetadata(
            intent="test-intent",
            invariants=["a"],
            constraints=["b"],
        )
        registry.register(pattern, metadata=metadata)
        snapshot = registry.metadata_snapshot()
        self.assertIn("test", snapshot)
        self.assertEqual(snapshot["test"]["intent"], "test-intent")
        self.assertEqual(snapshot["test"]["invariants"], ["a"])
        self.assertEqual(snapshot["test"]["constraints"], ["b"])

    def test_register_duplicate_raises(self) -> None:
        registry = PatternRegistry()
        pattern = PatternTransformation(name="dup", steps=["a"])
        registry.register(pattern)
        with self.assertRaises(ValueError):
            registry.register(pattern)


if __name__ == "__main__":
    unittest.main()
