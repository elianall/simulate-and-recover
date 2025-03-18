import math
import random
import unittest
from src import ez_diffusion

class TestEZDiffusion(unittest.TestCase):
    def test_simulate_ez_diffusion(self):
        # Use fixed parameters.
        a = 1.0
        v = 1.0
        t = 0.3
        results = ez_diffusion.simulate_ez_diffusion(a, v, t)
        y = math.exp(-a * v)
        expected_R = 1 / (y + 1)
        expected_M = t + (a**2 / v) * ((1 - y) / (y + 1))
        expected_V = (a**2 / (v**3)) * (1 - (2 * a * v * y + y**2) / ((y + 1)**2))
        self.assertAlmostEqual(results["R_pred"], expected_R, places=5)
        self.assertAlmostEqual(results["M_pred"], expected_M, places=5)
        self.assertAlmostEqual(results["V_pred"], expected_V, places=5)
    
    def test_recover_parameters(self):
        # Set seed for reproducibility.
        random.seed(0)
        a = 1.0
        v = 1.0
        t = 0.3
        a_est, v_est, t_est = ez_diffusion.recover_parameters(a, v, t)
        # Verify that recovered values fall within expected noise bounds.
        self.assertTrue(0.9 <= a_est <= 1.1)
        self.assertTrue(0.9 <= v_est <= 1.1)
        self.assertTrue(0.25 <= t_est <= 0.35)

    def test_simulate_and_recover(self):
        # Test that simulate_and_recover returns the correct number of iterations and keys.
        results = ez_diffusion.simulate_and_recover(10, iterations=5)
        self.assertEqual(len(results), 5)
        for res in results:
            for key in ["N", "iteration", "a", "v", "t", "R_pred", "M_pred", "V_pred", "a_est", "v_est", "t_est"]:
                self.assertIn(key, res)

if __name__ == "__main__":
    unittest.main()
