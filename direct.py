import numpy as np
import copy

def solve_direct(A, b):
    U = copy.copy(A)
    N = len(A)
    L = np.eye(N)

    for i in range(2, N + 1):
        for j in range(1, i):
            L[i - 1, j - 1] = U[i - 1, j - 1] / U[j - 1, j - 1]
            U[i - 1, :] = U[i - 1, :] - L[i - 1, j - 1] * U[j - 1, :]

    y = np.linalg.solve(L, b)
    x = np.linalg.solve(U, y)

    inorm = np.linalg.norm(np.matmul(A, x) - b)

    #print(inorm)

    return inorm