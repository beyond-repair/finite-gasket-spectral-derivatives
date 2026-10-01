"""W-derivatives of (1/2) Tr ln K from a list of Laplacian eigenvalues.

Does not select W. Does not build a continuum operator. Does not return a force.
"""

from __future__ import annotations

import math
from typing import Iterable


def require_positive(eigenvalues: Iterable[float], w: float, omega2: float = 1.0) -> list[float]:
    kappas = []
    for lam in eigenvalues:
        kappa = omega2 - w * lam
        if kappa <= 0.0:
            raise ValueError("K is not positive definite")
        kappas.append(kappa)
    return kappas


def gamma_loop(eigenvalues: Iterable[float], w: float, omega2: float = 1.0) -> float:
    kappas = require_positive(eigenvalues, w, omega2)
    return 0.5 * sum(math.log(k) for k in kappas)


def dgamma_dw(eigenvalues: Iterable[float], w: float, omega2: float = 1.0) -> float:
    require_positive(eigenvalues, w, omega2)
    return 0.5 * sum((-lam) / (omega2 - w * lam) for lam in eigenvalues)


def v_second(eigenvalues: Iterable[float], w: float, omega2: float = 1.0) -> float:
    require_positive(eigenvalues, w, omega2)
    return -0.5 * sum((lam * lam) / (omega2 - w * lam) ** 2 for lam in eigenvalues)
