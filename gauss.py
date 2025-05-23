import numpy as np

def solve_gauss(A, b):
    max_iterations = 1000
    diff = 1e-9
    x = np.ones_like(b)
    r_norm = np.zeros(max_iterations)
    iterations = 0

    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    T = D + L
    w = np.linalg.solve(T, b)
    T = T * -1
    inorm = np.linalg.norm(np.matmul(A, x) - b)
    r_norm[iterations] = inorm
    while iterations < max_iterations - 1 and inorm > diff:
        iterations += 1
        x = np.linalg.solve(T, np.matmul(U, x)) + w
        inorm = np.linalg.norm(np.matmul(A, x) - b)
        r_norm[iterations] = inorm

    return r_norm, iterations
