import numpy as np
import matplotlib.pyplot as plt


def main():

    a = -np.pi / 2
    b = np.pi / 2
    n = 1000
    h = (b - a) / (n - 1)
    x = np.arange(a, b + h, h)
    y = np.sin(x)
    m = 10

    XPN = np.array([x[0]])
    YPN = np.array([y[0]])

    dch = np.zeros(m)
    dp = np.zerox(m)
    

    for k in range(1, m + 1):

        # Chebyshev axe
        t = np.array([np.cos((2 * x - 1) * np.pi / (2 * k)) for x in range(1, k + 1)])
        XchN = (a + b) / 2 + (b - a) * t / 2
        YchN = np.sin(XchN)
        W = np.vander(XchN, increasing=True)
        A = np.linalg.solve(W, YchN)
        Pch = np.polyval(A, x)

        # Равномерные узлы
        W = np.vander(XPN)
        A = np.linalg.solve(W, YPN)
        Pp = np.polyval(A, x)
        XPN = np.linspace(a, b, k+1)
        YPN = np.sin(XPN)

        # Count accuracy