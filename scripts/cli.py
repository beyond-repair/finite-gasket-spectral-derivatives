"""Command line for the finite-gasket kernel.

``kernel``      evaluate Gamma_loop, dGamma/dW and V'' at a prescribed W, on the
                free Laplacian spectrum of build_gasket(level) or on a supplied
                eigenvalue list.
``decimation``  run the supporting numerics in check_decimation_hits.py.

W is always an input. Nothing here selects W, takes a continuum limit, or
returns a force. Exit codes: 0 ok, 2 bad input or K not positive definite.
"""
from __future__ import annotations

import argparse
import json
import math
import sys

from . import __version__
from .spectral_derivatives import dgamma_dw, gamma_loop, v_second

MAX_LEVEL = 7


def gasket_spectrum(level: int) -> list[float]:
    """Eigenvalues of free L = D - A on build_gasket(level), ascending."""
    import numpy as np

    from .check_decimation_hits import build_gasket, laplacian

    points, edges, _, _, _ = build_gasket(level)
    return [float(x) for x in np.linalg.eigvalsh(laplacian(len(points), edges))]


def _kernel(args) -> int:
    if args.eigenvalues is not None:
        source = "supplied eigenvalues"
        eigenvalues = [float(x) for x in args.eigenvalues.split(",") if x.strip()]
        if not eigenvalues:
            print("error: --eigenvalues is empty", file=sys.stderr)
            return 2
    else:
        if not 0 <= args.level <= MAX_LEVEL:
            print(f"error: --level must be between 0 and {MAX_LEVEL}", file=sys.stderr)
            return 2
        source = f"free L = D - A on build_gasket({args.level})"
        eigenvalues = gasket_spectrum(args.level)
    if not (math.isfinite(args.w) and math.isfinite(args.omega2)):
        print("error: --w and --omega2 must be finite", file=sys.stderr)
        return 2
    lam_max = max(eigenvalues)
    wall = args.omega2 / lam_max if lam_max > 0 else math.inf
    result = {
        "source": source,
        "N": len(eigenvalues),
        "lambda_min": min(eigenvalues),
        "lambda_max": lam_max,
        "W": args.w,
        "omega2": args.omega2,
        "spectral_wall": wall,
    }
    try:
        result["gamma_loop"] = gamma_loop(eigenvalues, args.w, args.omega2)
        result["dgamma_dw"] = dgamma_dw(eigenvalues, args.w, args.omega2)
        result["v_second"] = v_second(eigenvalues, args.w, args.omega2)
    except ValueError:
        print(
            f"error: K = omega2 I - W L is not positive definite at W={args.w} "
            f"(needs omega2 - W*lambda > 0 for every eigenvalue; wall omega2/lambda_max = {wall:.12g})",
            file=sys.stderr,
        )
        return 2
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"source        {result['source']}")
        print(f"N             {result['N']}")
        print(f"lambda range  [{result['lambda_min']:.12g}, {result['lambda_max']:.12g}]")
        print(f"W, omega2     {args.w:.12g}, {args.omega2:.12g}  (prescribed, not selected)")
        print(f"spectral wall {wall:.12g}")
        print(f"Gamma_loop    {result['gamma_loop']:.12g}")
        print(f"dGamma/dW     {result['dgamma_dw']:.12g}")
        print(f"V''(W)        {result['v_second']:.12g}")
    return 0


def _decimation(args) -> int:
    if not 1 <= args.nmax <= MAX_LEVEL:
        print(f"error: --nmax must be between 1 and {MAX_LEVEL}", file=sys.stderr)
        return 2
    from .check_decimation_hits import main as decimation_main

    decimation_main(args.nmax)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="gasket-spectral",
        description="W-derivatives of (1/2) Tr ln K on the finite gasket. W is an input; nothing is selected.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    k = sub.add_parser("kernel", help="Gamma_loop, dGamma/dW and V'' at a prescribed W")
    k.add_argument("--w", type=float, required=True, help="prescribed W (must satisfy omega2 - W*lambda_max > 0)")
    k.add_argument("--omega2", type=float, default=1.0, help="omega^2 (default 1)")
    group = k.add_mutually_exclusive_group()
    group.add_argument("--level", type=int, default=3, help=f"gasket level n, 0..{MAX_LEVEL} (default 3)")
    group.add_argument("--eigenvalues", help="comma-separated eigenvalue list instead of a gasket level")
    k.add_argument("--json", action="store_true", help="print JSON")
    k.set_defaults(func=_kernel)

    d = sub.add_parser("decimation", help="supporting decimation-hit numerics (numerical observation only)")
    d.add_argument("--nmax", type=int, default=6, help=f"highest level, 1..{MAX_LEVEL} (default 6)")
    d.set_defaults(func=_decimation)
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
