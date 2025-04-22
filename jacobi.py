import numpy as np
def solve_jacobi(A, b):
    max_iterations = 1000
    diff = 1e-9
    x = np.zeros_like(b)
    r_norm = np.zeros(max_iterations)


    # x(k + 1) = -D^(-1) * (L + U) * x(k) + D^(-1) * b

    L = np.tril(A, -1)
    U = np.triu(A, 1)
    D = np.diag(np.diag(A))
    D = np.linalg.inv(D)
    w = D * b
    M = (L + U) * (D * -1)
    for i in range(max_iterations):
        x_new = np.dot(M, x) + w
        r_norm[i] = np.linalg.norm(x_new - x)
        if r_norm[i] < diff:
            break
        x = x_new

