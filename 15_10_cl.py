import numpy as np
import matplotlib.pyplot as plt
from math import pow


# def f(x: np.ndarray) -> np.ndarray:
#     return -np.power(x, 5) + 3 * np.power(x, 4) + 4 * np.power(x, 3) - 2 * np.power(x, 2) - 5 * x -1


# def F(x: np.ndarray) -> np.ndarray:
#     return (-np.power(x, 6) / 6) + 2.4 * np.power(x, 5) + 3 * np.power(x, 4) - (4 / 3) * np.power(x, 3) - 2.5 * np.power(x, 2) - x

def f(x: float) -> float:
    return -pow(x, 5) + 3 * pow(x, 4) + 4 * pow(x, 3) + 2 * pow(x, 2) - 5 * x - 1

def F(x: float) -> float:
    return (-1 / 6) * pow(x, 6) + (3 / 5) * pow(x, 5) + pow(x, 4) - (2 / 3) * pow(x, 3) - (5 / 2) * pow(x, 2) - x

def main():
    n = 6
    a, b = -1, 1
    I = ((b - a) / 6) * f(a) + ((4 * (b - a)) / 6) * f((a + b) / 2) + ((b - a) / 6) * f(b)
    print(I, F(b) - F(a))




if __name__ == '__main__':
    main()
