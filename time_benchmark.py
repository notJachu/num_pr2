import time

from direct import solve_direct
from jacobi import solve_jacobi
from gauss import solve_gauss
from utils import fill_matrix, fill_b, plot_time_log, plot_time_normal


def test_times(N):
    time_jacobi = []
    time_gauss = []
    time_direct = []
    for n in N:
        A = fill_matrix(n, 12, -1, -1)
        b = fill_b(n)

        # Jacobi
        start = time.time()
        solve_jacobi(A, b)
        end = time.time()
        time_jacobi.append(end - start)

        # Gauss-Seidel
        start = time.time()
        solve_gauss(A, b)
        end = time.time()
        time_gauss.append(end - start)

        # Direct
        start = time.time()
        solve_direct(A, b)
        end = time.time()
        time_direct.append(end - start)

    plot_time_log(time_jacobi, time_gauss, time_direct, N)
    plot_time_normal(time_jacobi, time_gauss, time_direct, N)
    return time_jacobi, time_gauss, time_direct
