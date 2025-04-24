import matplotlib.pyplot as plt
import numpy as np

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


def plot_time_log(time_jacobi, time_gauss, time_direct, N):

    plt.figure(figsize=(10, 6))

    plt.plot(N, time_jacobi, marker='o', label='Jacobi')
    plt.plot(N, time_gauss, marker='s', label='Gauss-Seidel')
    plt.plot(N, time_direct, marker='^', label='Direct')

    plt.yscale('log')

    plt.xlabel('Matrix Size (N)')
    plt.ylabel('Computation Time (s)')
    plt.title('Computation Time vs Matrix Size (Log Scale)')
    plt.xticks(N, labels=[str(n) for n in N])
    plt.legend()

    plt.tight_layout()
    plt.show()

    return

def plot_time_normal(time_jacobi, time_gauss, time_direct, N):
    plt.figure(figsize=(10, 6))

    plt.plot(N, time_jacobi, marker='o', label='Jacobi')
    plt.plot(N, time_gauss, marker='s', label='Gauss-Seidel')
    plt.plot(N, time_direct, marker='^', label='Direct')


    plt.xlabel('Matrix Size (N)')
    plt.ylabel('Computation Time (s)')
    plt.title('Computation Time vs Matrix Size (Normal Scale)')
    plt.xticks(N, labels=[str(n) for n in N])
    plt.legend()

    plt.tight_layout()
    plt.show()

    return