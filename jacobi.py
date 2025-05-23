import numpy as np
def solve_jacobi(A, b):
    max_iterations = 1000
    diff = 1e-9
    x = np.ones_like(b)
    r_norm = np.zeros(max_iterations)
    iterations = 0

    # x(k + 1) = -D^(-1) * (L + U) * x(k) + D^(-1) * b

    L = np.tril(A, -1)
    U = np.triu(A, 1)
    D = np.diag(np.diag(A))

    # inverse of a diagonal is inverse of its elements so i can just O(n) it
    for i in range(len(D)):
        D[i][i] = 1 / D[i][i]
    w = np.matmul(D, b)
    M = L + U
    D = D * -1
    M = np.matmul(D, M)
    inorm = np.linalg.norm(np.matmul(A, x) - b)
    r_norm[iterations] = inorm
    while iterations < max_iterations - 1 and inorm > diff:
        iterations += 1
        x = np.matmul(M, x) + w
        inorm = np.linalg.norm(np.matmul(A, x) - b)
        r_norm[iterations] = inorm
    
    
    return r_norm, iterations

