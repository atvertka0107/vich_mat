import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

a = -9*np.pi/2
b = 9*np.pi/2
n = 1000
h = (b - a) / (n - 1)

x = np.linspace(a, b, n)
y = np.cos(x)

m = 10
n_sp = 52

# Узлы Чебышева
t = np.cos((2 * np.arange(1, m + 2) - 1) * np.pi / (2 * (m + 1)))
XchN = (a + b) / 2 + (b - a) * t / 2
YchN = np.cos(XchN)

# Полином Чебышева
Ach = np.polyfit(XchN, YchN, m)
Pch = np.polyval(Ach, x)

# Равномерные узлы
Xp = np.linspace(a, b, m + 1)
Yp = np.cos(Xp)

# Полином для равномерных узлов
Ap = np.polyfit(Xp, Yp, m)
Pp = np.polyval(Ap, x)

# Построение графиков ошибки полиномов
plt.plot(x, np.abs(y - Pch), 'r', label="Узлы Чебышева")
plt.plot(x, np.abs(y - Pp), 'b', label="Равномерные узлы")

# Сплайн
Xsp = np.linspace(a, b, n_sp + 1)
Ysp = np.cos(Xsp)
spline = CubicSpline(Xsp, Ysp)
Spl = spline(x)

# Построение графика ошибки сплайна
plt.plot(x, np.abs(y - Spl), 'g', label="Кубический сплайн")

# Настройки графика
plt.legend()
plt.xlabel('x')
plt.ylabel('Погрешность')
plt.show()