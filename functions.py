import sympy as sp
import numpy as np


def f(arg):
    return arg ** 2 + 4 * np.sin(float(arg))


# Нашли эквивалентную функцию
def phi(arg):
    return np.arcsin(((-1)*float(arg)**2)/4)        # - только c нулем работает
                                                    #np.sqrt(4*np.sin((-1)*float(arg))) - расходится
                                                    #-4 * np.sin(float(arg))/arg - расходится


def df(x):  # Производная f(x)
    return 2*x + 4 * np.cos(float(x))


def Iteration(xn, epsilon, k):
    while True:
        k += 1
        xn_next = phi(xn)
        if abs(xn_next - xn) <= epsilon:
            return xn_next, k
        xn = xn_next


def Newton(x0, epsilon, k):
    x = x0
    while True:
        k += 1
        x_next = x - f(x) / df(x)

        if abs(x_next - x) < epsilon:
            return x_next , k

        x = x_next


def Dihotomia(a, b, epsilon, k):
    while (b - a) / 2 > epsilon:                # Делим интервал пополам пока он больше Эпсилон
        k += 1
        c = (a + b) / 2
        if f(c) == 0:
            return c, k                        # Нашли точный корень либо
        elif f(a) * f(c) < 0:
            b = c                           # Корень в [a, c]
        else:
            a = c                           # Корень в [c, b]

    return (a + b) / 2, k

