import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from functions import *

function = "x^2 + 4*sin(x)"
diff1 = sp.diff(function, sp.Symbol('x'), 1)
diff2 = sp.diff(function, sp.Symbol('x'), 2)

print("Функция: ", function)
print("Первая производная = ", diff1)
print("Вторая производная = ", diff2)

print("\n-----------------------Отделение Корней---------------------------")

x_min, x_max = -5, 5                # Сначала проверим аналитически
step = 0.21

x_values = np.arange(x_min, x_max, step)

intervals = []
pred_x = x_values[0]
pred_y = f(pred_x)

for x in x_values[1:]:
    y = f(x)

    if pred_y * y < 0:
        intervals.append([sp.simplify(pred_x), sp.simplify(x)])

    pred_x, pred_y = x, y

print("Найденные интервалы, где функция меняет знак: \n", intervals)

x = np.linspace(-5, 5, 1000)
y = x ** 2 + 4 * np.sin(x)
y0 = np.zeros(1000)

plt.title('График', fontsize=14, fontname='Times New Roman')
plt.plot(x, y, color="red", label="x^2 + 4*sin(x)")
plt.plot(x, y0, '--', color="green", label="y = 0")
plt.grid()
plt.legend()
plt.show()                 # теперь построим график и убедимся сами

epsilon = np.double(input("Введите Эпсилон: "))

print('\n-----------------------Метод простой итерации-----------------------')
k = 0

x1, k = Iteration(intervals[0][1], epsilon, k)          # Если подставить левую границу не будет сходиться даже к нулю
print(f"1-й Корень:{x1:.10f} \tбыл найдем через {k} итераций")


x2, k = Iteration(intervals[1][1], epsilon, k)
print(f"2-й Корень:{x2:.10f} \tбыл найдем через {k} итераций")

print("\n---------------------------Метод Ньютона---------------------------")

if df(intervals[0][0])*intervals[0][0] > 0:
    x1, k = Newton(intervals[0][0], epsilon, k)
elif df(intervals[0][1]) * intervals[0][1] > 0:
    x1, k = Newton(intervals[0][1], epsilon, k)
print(f"1-й Корень: {x1:.10f} \tбыл найдем через {k} итераций")

if df(intervals[1][0])*intervals[1][0] > 0:
    x2, k = Newton(intervals[1][0], epsilon, k)
elif df(intervals[1][1])*intervals[1][1] > 0:
    x2, k = Newton(intervals[1][1], epsilon, k)
print(f"2-й Корень: {x2:.10f} \tбыл найдем через {k} итераций")


print("\n---------------------------Метод Дихотомии---------------------------")
k = 0

x1, k = Dihotomia(intervals[0][0], intervals[0][1], epsilon, k)
print(f"1-й Корень: {x1:.10f} \tбыл найдем через {k} итераций")

x2, k = Dihotomia(intervals[1][0], intervals[1][1], epsilon, k)
print(f"2-й Корень: {x2:.10f} \tбыл найдем через {k} итераций")
