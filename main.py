import sympy as sp
import matplotlib.pyplot as plt
from functions import *
import subprocess

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

root1 = [0, -1.93375376282]
root2 = [0, 0]

plt.title('График', fontsize=14, fontname='Times New Roman')
plt.plot(x, y, color="red", label="x^2 + 4*sin(x)")
plt.plot(x, y0, '--', color="green", label="y = 0")
plt.scatter(root1, root2, color='blue', label='Найденные корни')
plt.grid()
plt.legend()
plt.show()

# Теперь построим график производных для каждой фи и убедимся сами что они ограничены единицей

subprocess.run(["python", "diff_phi.py"])

epsilon = np.double(input("Введите Эпсилон: "))

print('\n-----------------------Метод простой итерации-----------------------')
k = 0

x1, k = Iteration1(intervals[0][1], epsilon, k)          # Если подставить левую границу не будет сходиться даже к нулю
print(f"1-й Корень:{x1:.10f} \tбыл найдем через {k} итераций")


x2, k = Iteration2(intervals[1][1], epsilon, k)
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
