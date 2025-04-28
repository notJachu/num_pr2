# 1 9 7 7 4 1
# 1 2 3 4 5 6

# A = NxN, N = 1241
# r <= 10e-9

# a1 = 5 + 7 = 12
# a2 = a3 = -1
# b = [N]
# b[n] = sin(n * (7 + 1))

from jacobi import solve_jacobi
from gauss import solve_gauss
from direct import solve_direct
from utils import fill_matrix, fill_b, plot_rnorm_log
from time_benchmark import test_times

def main():


    # A
    A = fill_matrix(1241, 12, -1, -1)
    b = fill_b(1241)

    # B + D
    # rnorm, iterations = solve_jacobi(A, b)
    # plot_rnorm_log(rnorm, iterations, "Jacobi")
    # rnorm, iterations = solve_gauss(A, b)
    # plot_rnorm_log(rnorm, iterations, "Gauss-Seidel")
    # inorm = solve_direct(A, b)
    # print(inorm)

    # C
    # A = fill_matrix(1241, 3, -1, -1)
    # rnorm, iterations = solve_jacobi(A, b)
    # plot_rnorm_log(rnorm, iterations, "Jacobi")
    # rnorm, iterations = solve_gauss(A, b)
    # plot_rnorm_log(rnorm, iterations, "Gauss-Seidel")

    # E
    N = [100, 200, 500, 1000, 2000, 3000, 5000]
    test_times(N)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
