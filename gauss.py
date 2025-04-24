import numpy as np
import matplotlib.pyplot as plt

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
    while iterations < max_iterations and inorm > diff:
        iterations += 1
        x = np.linalg.solve(T, np.matmul(U, x)) + w
        inorm = np.linalg.norm(np.matmul(A, x) - b)
        r_norm[iterations] = inorm

    print(iterations)

    print(r_norm)
    fig, ax = plt.subplots()
    ax.plot(r_norm[:iterations])
    ax.set_yscale('log')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Residual Norm')
    ax.set_title('Gauss-Seidel Method Residual Norm')
    plt.show()

    return