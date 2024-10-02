import numpy as np
import matplotlib.pyplot as plt


def main():

    a = -np.pi / 2
    b = np.pi / 2
    n = 1000
    x = np.linspace(a, b, n)
    y = np.cos(x) 
    m = 30
    pogr = np.zeros(m)

    XN = np.array([x[0]])
    YN = np.array([y[0]])

    plt.figure('Погрешность[i]')

    for k in range(1, m + 1):

        W = np.vander(XN)
        A = np.linalg.solve(W, YN)
        P = np.polyval(A, x)
        pogr[k - 1] = np.max(np.abs(P  - y))

        XN = np.linspace(a, b, k+1)
        YN = np.cos(XN)

        plt.subplot(5, m // 5, k)
        plt.plot(x, np.abs(P - y))
        plt.title(f'k={k}')
    
    plt.subplots_adjust(hspace=0.7)

    plt.figure('Погрешность')
    ax = plt.subplot()
    ax.set_xticks(np.arange(1, m + 1))
    ax.plot(np.arange(1, m + 1), np.log10(pogr), 'purple')
    plt.xlabel('Количество точек')
    plt.ylabel('log10(погрешность)')
    plt.show()



if __name__ == '__main__':
    main()
