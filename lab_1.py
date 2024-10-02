import matplotlib.pyplot as plt
import numpy as np
from random import randint

a = -np.pi / 2
b = np.pi / 2


k = 1000
h = (b - a) / (k - 1)

x = np.linspace(a, b, k)
y = np.sin(x)

XN = np.array([x[0]])
YN = np.array([y[0]])

m = 15
pogr = np.zeros(m)

plt.figure()
for k in range(1, m + 1):
    W = np.vander(XN)
    A = np.linalg.solve(W, YN)

    P = np.polyval(A, x)
    pogr[k - 1] = np.max(np.abs(y - P))

    hx = (b - a) / k
    XN = np.linspace(a, b, k + 1)
    YN = np.sin(XN) # + randint(10, 50) / 100 # add inaccuracy here

    plt.subplot(5, int(m/5), k)

    # plt.plot(XN, YN)
    plt.plot(x, np.abs(y - P), 'b')
    plt.title(f'point_cnt = {k}')

plt.subplots_adjust(hspace=0.7)

plt.figure()
ax = plt.subplot()
ax.set_xticks(np.arange(1, m+1))
ax.plot(np.arange(1, m+1), np.log10(pogr), 'r')
plt.xlabel('Количество точек')
plt.ylabel('Погрешность')
plt.show()