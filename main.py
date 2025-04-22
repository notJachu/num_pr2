# 1 9 7 7 4 1
# 1 2 3 4 5 6

# A = NxN, N = 1241
# r <= 10e-9

# a1 = 5 + 7 = 12
# a2 = a3 = -1
# b = [N]
# b[n] = sin(n * (7 + 1))

#TODO:
# B. solve jacobi, gauss-seidel + r_norm plot log scale
# C. a1 = 3, a2 = a3 = -1 + plot
# D. direct LU + plot
# E. plot all 3 for N = {100, 500, 1000, 2000, 3000, ... } log scale and normal

import numpy as np
from jacobi import solve_jacobi
from gauss import solve_gauss

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

def main():
    A = fill_matrix(1241, 12, -1, -1)
    b = fill_b(1241)
    solve_jacobi(A, b)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
