#!/usr/bin/env python3
import math
import numpy as np
import itertools


def levi_civita_3d() -> np.ndarray:
    eps = np.zeros((3, 3, 3), dtype=int)
    for i, j, k in itertools.permutations(range(3), 3):
        perm = (i, j, k)
        inv_count = 0
        for a in range(3):
            for b in range(a + 1, 3):
                if perm[a] > perm[b]:
                    inv_count += 1
        eps[i, j, k] = -1 if inv_count % 2 else 1
    return eps


def compute_E_det_ABC_squared():
    eps = levi_civita_3d()
    delta = np.eye(3)
    lam = 1.0 / 3.0  # λ = 1/3

    T = 0.0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for p in range(3):
                    for q in range(3):
                        for r in range(3):
                            T += (
                                eps[i, j, k]
                                * eps[p, q, r]
                                * lam * delta[i, p]
                                * lam * delta[j, q]
                                * lam * delta[k, r]
                            )
    return T  


def main():
    T = compute_E_det_ABC_squared()
    print(f"E[det(A,B,C)^2] = {T} (theory: 2/9 ≈ {2/9:.6f})")

    E_V2 = T / 9.0
    print(f"E[V_ABCD^2] = {E_V2} (theory: 2/81 ≈ {2/81:.6f})")

    rms_V = math.sqrt(E_V2)
    print(f"sqrt(E[V_ABCD^2]) = {rms_V} (theory: sqrt(2)/9 ≈ {math.sqrt(2)/9:.6f})")


if __name__ == "__main__":
    main()
