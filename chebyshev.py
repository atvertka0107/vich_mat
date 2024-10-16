import numpy as np
import matplotlib.pyplot as plt


def main():

    a = 0
    b = np.pi
    n = 1000
    h = (b - a) / (n - 1)
    x = np.arange(a, b + h, h)
    y = np.cos(x)
    m = 10
        
    XPN = np.array([x[0]])
    YPN = np.array([y[0]])

    dch = np.zeros(m)
    dp = np.zeros(m)

    fig, ax = plt.subplots(10, 2)
    ax[0][0].set_title('x=x_0 + nh')
    ax[0][1].set_title('Chebyshev')

    for k in range(1, m + 1):

        # Chebyshev axe
        t = np.array([np.cos((2 * j - 1) * np.pi / (2 * k)) for j in range(1, k + 1)])
        XchN = (a + b) / 2 + (b - a) * t / 2
        YchN = np.cos(XchN)
        Wch = np.vander(XchN)
        Ach = np.linalg.solve(Wch, YchN)
        Pch = np.polyval(Ach, x)

        # Равномерные узлы
        W = np.vander(XPN)
        A = np.linalg.solve(W, YPN)
        Pp = np.polyval(A, x)
        XPN = np.linspace(a, b, k+1)
        YPN = np.cos(XPN)

        # HERE plot graph
        ax[k - 1][0].plot(x, np.abs(y - Pp))
        ax[k - 1][1].plot(x, np.abs(y - Pch))


        # Count accuracy
        dch[k - 1] = np.max(np.abs(y - Pch))
        dp[k - 1] = np.max(np.abs(y - Pp))

    fig.show()
    # Print other graph
    plt.figure()
    ax = plt.subplot()
    ax.set_xticks(np.arange(1, m+1))
    ax.plot(np.arange(1, m+1), np.log10(dp), 'b', label='Равномерные узлы')
    ax.plot(np.arange(1, m+1), np.log10(dch), 'r', label='Узлы Чебышёва')
    plt.legend()
    plt.xlabel('Количество точек')
    plt.ylabel('Погрешность')
    plt.show()


if __name__ == '__main__':
    main()
