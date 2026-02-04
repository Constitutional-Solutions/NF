import unittest

from genesis_kernel.spiral_physics import SpiralLaws


class TestSpiralPhysics(unittest.TestCase):
    def setUp(self):
        self.engine = SpiralLaws()

    def test_growth(self):
        r1 = self.engine.law_of_growth(1.0)
        r2 = self.engine.law_of_growth(2.0)
        self.assertGreater(r2, r1)

    def test_resonance(self):
        c = self.engine.law_of_resonance([1, 2, 3], [2, 4, 6])
        self.assertAlmostEqual(c, 1.0)

    def test_emergence(self):
        state = self.engine.law_of_emergence(3.14, [1, 0], [0.9, 0.1])
        self.assertEqual(state.mode, "ORDER")


if __name__ == "__main__":
    unittest.main()
