import numpy as np


def f(arg):  # Функция
    return arg ** 2 + 4 * np.sin(float(arg))


def df(x):  # Производная f(x)
    return 2 * x + 4 * np.cos(float(x))


def df2(x):  # Вторая
    return 2 * (1 - 2 * np.sin(float(x)))


# Нашел функцию, которая сходится именно к корню -1,9375
def phi1(arg):
    return -1 * np.sqrt(4 * np.sin((-1) * float(arg)))


# Старую перенес сюда (которая сходится к нолю)
def phi2(arg):
    return np.arcsin(((-1) * float(arg) ** 2) / 4)


def Iteration1(xn, epsilon, k):
    while True:
        k += 1
        xn_next = phi1(xn)
        if abs(xn_next - xn) <= epsilon:
            return xn_next, k
        xn = xn_next


def Iteration2(xn, epsilon, k):
    while True:
        k += 1
        xn_next = phi2(xn)
        if abs(xn_next - xn) <= epsilon:
            return xn_next, k
        xn = xn_next


def Newton(x0, epsilon, k):
    x = x0
    while True:
        k += 1
        x_next = x - f(x) / df(x)

        if abs(x_next - x) <= epsilon:
            return x_next, k

        x = x_next


def Dihotomia(a, b, epsilon, k):
    while (b - a) / 2 > epsilon:                # Делим интервал пополам пока он больше Эпсилон
        k += 1
        c = (a + b) / 2
        if abs(f(c)) <= epsilon:
            return c, k                        # Нашли точный корень либо
        elif f(a) * f(c) < 0:
            b = c                           # Корень в [a, c]
        else:
            a = c                           # Корень в [c, b]

    return (a + b) / 2, k


def ChordMethod(a, b, epsilon, k):
    if f(a) > 0:                # Выбираем неподвижный конец отрезка в зависимости от знака
        x_fixed, xn = a, b
    else:
        x_fixed, xn = b, a

    while True:
        k += 1
        x_next = xn - (f(xn) * (xn - x_fixed)) / (f(xn) - f(x_fixed))

        if abs(x_next - xn) <= epsilon:
            return x_next, k

        xn = x_next


def Chebishev(x0, epsilon, k):
    x = x0
    while True:
        k += 1
        x_next = x - f(x) / df(x) - (df2(x) * f(x) ** 2) / (2 * df(x) ** 3)

        if abs(x_next - x) <= epsilon:
            return x_next, k

        x = x_next


def check(root, epsilon):
    if abs(f(root)) < epsilon:
        return "Найден верно."
    else:
        return "Найден неверно."

