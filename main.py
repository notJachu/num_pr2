# 1 9 7 7 4 1
# 1 2 3 4 5 6

# A = NxN, N = 1241
# r <= 10e-9

# a1 = 5 + 7 = 12
# a2 = a3 = -1
# b = [N]
# b[n] = sin(n * (7 + 1))

#TODO:
# E. plot tome for all 3 for N = {100, 500, 1000, 2000, 3000, ... } log scale and normal

import numpy as np
from jacobi import solve_jacobi
from gauss import solve_gauss
from direct import solve_direct
import matplotlib.pyplot as plt

def fill_matrix(N, a1, a2, a3):
    A = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i][j] = a1
            elif abs(i - j) == 1:
                A[i][j] = a2
            elif abs(i - j) == 2:
                A[i][j] = a3
    return A

def fill_b(N):
    b = np.zeros(N)
    for i in range(N):
        b[i] = np.sin(i * (7 + 1))
    return b

def plot_rnorm_log(rnorm, iterations, method_name):
    fig, ax = plt.subplots()
    ax.plot(rnorm[:iterations])
    ax.set_yscale('log')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Residual Norm')
    ax.set_title(f'{method_name} Method Residual Norm')
    plt.show()

def main():
    # A
    A = fill_matrix(1241, 12, -1, -1)
    b = fill_b(1241)

    # B + D
    rnorm, iterations = solve_jacobi(A, b)
    plot_rnorm_log(rnorm, iterations, "Jacobi")
    rnorm, iterations = solve_gauss(A, b)
    plot_rnorm_log(rnorm, iterations, "Gauss-Seidel")
    solve_direct(A, b)

    # C
    A = fill_matrix(1241, 3, -1, -1)
    solve_jacobi(A, b)
    solve_gauss(A, b)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
