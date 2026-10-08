"""CLI checks for gasket-spectral (python -m gasket_spectral / python -m scripts).

Numerical checks of the shipped commands only. They do not prove the README
theorems, select W, or assert a force.
"""
from __future__ import annotations

import contextlib
import importlib
import io
import json
import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

try:
    pkg = importlib.import_module("gasket_spectral")
except ImportError:  # plain checkout without pip install
    sys.path.insert(0, str(ROOT))
    pkg = importlib.import_module("scripts")
cli = importlib.import_module(pkg.__name__ + ".cli")
kernel = importlib.import_module(pkg.__name__ + ".spectral_derivatives")


def run(*argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            code = cli.main(list(argv))
        except SystemExit as exc:  # argparse errors
            code = exc.code
    return code, out.getvalue(), err.getvalue()


class GasketSpectrumTests(unittest.TestCase):
    def test_vertex_count_matches_constructor_formula(self):
        for n in range(1, 5):
            self.assertEqual(len(cli.gasket_spectrum(n)), (3 ** (n + 1) + 3) // 2)

    def test_lambda_max_is_six_for_n_at_least_two(self):
        for n in range(2, 6):
            self.assertAlmostEqual(max(cli.gasket_spectrum(n)), 6.0, places=9)

    def test_free_mult6_matches_readme_formula_numerically(self):
        for n in range(2, 6):
            mult6 = sum(1 for lam in cli.gasket_spectrum(n) if abs(lam - 6.0) < 1e-8)
            self.assertEqual(mult6, (3 ** n - 3) // 2)


class KernelCommandTests(unittest.TestCase):
    def test_json_matches_kernel_functions(self):
        code, out, err = run("kernel", "--level", "3", "--w", "0.1", "--json")
        self.assertEqual(code, 0, err)
        data = json.loads(out)
        ev = cli.gasket_spectrum(3)
        self.assertEqual(data["N"], 42)
        self.assertAlmostEqual(data["gamma_loop"], kernel.gamma_loop(ev, 0.1), places=12)
        self.assertAlmostEqual(data["dgamma_dw"], kernel.dgamma_dw(ev, 0.1), places=10)
        self.assertAlmostEqual(data["v_second"], kernel.v_second(ev, 0.1), places=8)
        self.assertAlmostEqual(data["spectral_wall"], 1 / 6, places=12)
        self.assertLess(data["v_second"], 0.0)

    def test_supplied_eigenvalues_reproduce_lambda6_split(self):
        code, out, err = run("kernel", "--eigenvalues", "0,2,6,6", "--w", "0.1", "--json")
        self.assertEqual(code, 0, err)
        data = json.loads(out)
        self.assertAlmostEqual(data["gamma_loop"], math.log(1 - 0.6) + 0.5 * math.log(1 - 0.2), places=12)

    def test_wall_and_beyond_exit_2(self):
        for w in ("0.16666666666666667", "0.2"):
            code, out, err = run("kernel", "--level", "2", "--w", w)
            self.assertEqual(code, 2)
            self.assertIn("not positive definite", err)
            self.assertEqual(out, "")

    def test_omega2_moves_the_wall(self):
        code, _, err = run("kernel", "--level", "2", "--w", "0.5", "--omega2", "4", "--json")
        self.assertEqual(code, 0, err)
        code, _, _ = run("kernel", "--level", "2", "--w", "0.7", "--omega2", "4")
        self.assertEqual(code, 2)

    def test_bad_inputs_exit_2(self):
        self.assertEqual(run("kernel", "--level", "99", "--w", "0.1")[0], 2)
        self.assertEqual(run("kernel", "--eigenvalues", "", "--w", "0.1")[0], 2)
        self.assertEqual(run("kernel", "--w", "nan")[0], 2)
        self.assertEqual(run("kernel")[0], 2)  # W is required, never defaulted
        self.assertEqual(run()[0], 2)

    def test_text_output_says_w_is_prescribed(self):
        code, out, _ = run("kernel", "--level", "1", "--w", "-0.3")
        self.assertEqual(code, 0)
        self.assertIn("prescribed, not selected", out)


class DecimationCommandTests(unittest.TestCase):
    def test_decimation_numerics_run(self):
        code, out, err = run("decimation", "--nmax", "4")
        self.assertEqual(code, 0, err)
        self.assertIn("n=4 N=123 exc=64 hit=19 nonhit=40 c_n=41", out)
        self.assertIn("exact rational Krylov dim c_2 = 11", out)
        self.assertIn("exact rational Krylov dim c_3 = 21", out)

    def test_decimation_bad_nmax(self):
        self.assertEqual(run("decimation", "--nmax", "0")[0], 2)


if __name__ == "__main__":
    unittest.main()
