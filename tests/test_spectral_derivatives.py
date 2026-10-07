"""Kernel checks for scripts/spectral_derivatives.py.

Does not construct a gasket, select W, or assert a force.
"""

from __future__ import annotations

import importlib.util
import math
import unittest
from pathlib import Path


def _load():
    path = Path(__file__).resolve().parents[1] / "scripts" / "spectral_derivatives.py"
    spec = importlib.util.spec_from_file_location("spectral_derivatives", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SpectralDerivativeTests(unittest.TestCase):
    def setUp(self):
        self.mod = _load()
        self.ev = [0.0, 2.0, 6.0, 6.0]
        self.w = 0.1

    def test_positive_guard_rejects_spectral_wall(self):
        with self.assertRaises(ValueError):
            self.mod.require_positive(self.ev, 1.0 / 6.0)

    def test_first_derivative_matches_central_difference(self):
        h = 1e-6
        analytic = self.mod.dgamma_dw(self.ev, self.w)
        finite = (
            self.mod.gamma_loop(self.ev, self.w + h)
            - self.mod.gamma_loop(self.ev, self.w - h)
        ) / (2 * h)
        self.assertAlmostEqual(analytic, finite, places=6)

    def test_second_derivative_matches_central_difference(self):
        h = 1e-6
        analytic = self.mod.v_second(self.ev, self.w)
        finite = (
            self.mod.dgamma_dw(self.ev, self.w + h)
            - self.mod.dgamma_dw(self.ev, self.w - h)
        ) / (2 * h)
        self.assertAlmostEqual(analytic, finite, places=5)

    def test_lambda6_split_identity(self):
        w = self.w
        direct = self.mod.gamma_loop(self.ev, w)
        split = math.log(1 - 6 * w) + 0.5 * math.log(1 - w * 2.0)
        self.assertAlmostEqual(direct, split, places=12)
        self.assertLess(self.mod.v_second(self.ev, w), 0.0)

    def test_omega2_scales_the_positive_wall(self):
        omega2 = 4.0
        self.mod.require_positive(self.ev, 0.5, omega2)
        with self.assertRaises(ValueError):
            self.mod.require_positive(self.ev, omega2 / 6.0, omega2)
        analytic = self.mod.dgamma_dw(self.ev, 0.2, omega2)
        h = 1e-6
        finite = (
            self.mod.gamma_loop(self.ev, 0.2 + h, omega2)
            - self.mod.gamma_loop(self.ev, 0.2 - h, omega2)
        ) / (2 * h)
        self.assertAlmostEqual(analytic, finite, places=6)


if __name__ == "__main__":
    unittest.main()
