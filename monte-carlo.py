import numpy as np
import math
import statistics

def random_point_on_sphere():
    # Равномерная точка на S^2: нормальный вектор и нормировка
    v = np.random.normal(size=3)
    return v / np.linalg.norm(v)

def tetrahedron_volume(a, b, c, d):
    # V = |det(b-a, c-a, d-a)| / 6
    mat = np.stack([b - a, c - a, d - a], axis=1)  # матрица 3x3
    det = np.linalg.det(mat)
    return abs(det) / 6.0

def main():
    n = 100000  # число испытаний
    vols = []
    for _ in range(n):
        A = random_point_on_sphere()
        B = random_point_on_sphere()
        C = random_point_on_sphere()
        D = random_point_on_sphere()
        v = tetrahedron_volume(A, B, C, D)
        vols.append(v)

    mean_v = statistics.mean(vols)
    mean_v2 = statistics.mean([v*v for v in vols])
    print(f"E[|V|] ≈ {mean_v}")
    print(f"E[V^2] ≈ {mean_v2}")
    print(f"sqrt(E[V^2]) ≈ {math.sqrt(mean_v2)}")

if __name__ == "__main__":
    main()
