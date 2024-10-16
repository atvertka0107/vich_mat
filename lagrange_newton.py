import numpy as np
import matplotlib.pyplot as plt


def lagrange(x_values: list[float], y_values: list[float], x: float) -> float:
    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result


def diff(x: list[float], y: list[float]):
    n = len(y)
    table = np.zeros((n, n))
    table[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])
    return table[0]


def newton(x: list[float], y: list[float], xi: float):
    coeffs = diff(x, y)
    n = len(coeffs)
    sum = coeffs[0]
    for i in range(1, n):
        term = coeffs[i]
        for j in range(i):
            term *= (xi - x[j])
        sum += term
    return sum

def main() -> None:
    a = -3 * np.pi
    b = 3 * np.pi
    n = 1000
    x = np.linspace(a, b, n)
    y = np.cos(x)
    m = 15

    XN = [x[0]]
    YN = [y[0]]
    pogr_L = np.zeros(m)
    pogr_N = np.zeros(m)
    pogr_G = np.zeros(m)

    for k in range(1, m + 1):
        W = np.vander(XN)
        A = np.linalg.solve(W, YN)
        P = np.polyval(A, x)
        pogr_G[k - 1] = np.max(np.abs(y - P))
        L = np.array([lagrange(XN, YN, x_i) for x_i in x])
        N = np.array([newton(XN, YN, x_i) for x_i in x])
        pogr_L[k - 1] = np.max(np.abs(y - L))
        pogr_N[k - 1] = np.max(np.abs(y - N))
        XN = np.linspace(a, b, k + 1)
        YN = np.cos(XN)

    plt.figure('Ньютон Лфгранж')
    ax = plt.subplot()
    ax.set_xticks(np.arange(1, m+1))
    ax.plot(np.arange(1, m + 1), np.log10(pogr_L), 'r', label='Лагранж')
    ax.plot(np.arange(1, m + 1), np.log10(pogr_N), 'b', linestyle=':', label='Ньютон')
    ax.plot(np.arange(1, m + 1), np.log10(pogr_G), linestyle='-.', label='Гаус')
    plt.xlabel('Количество точек')
    plt.ylabel('log10(погрешность)')
    plt.title('a=0 b=pi')
    ax.legend()
    plt.show()



if __name__ == '__main__':
    main()
