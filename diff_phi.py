import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')


function_phi1 = sp.sympify("-1 * sqrt(4*sin(-1*x))")
diff_func1 = sp.diff(function_phi1, x)

function_phi2 = sp.sympify("asin((-x**2)/4)")
diff_func2 = sp.diff(function_phi2, x)

intervals = [[-2.06000000000000, -1.85000000000000], [-0.170000000000001, 0.0399999999999991]]

x_phi1 = np.linspace(intervals[0][0], intervals[0][1], 100)
x_phi2 = np.linspace(intervals[1][0], intervals[1][1], 100)

y_phi1 = [
    float(diff_func1.subs(x, val).evalf()) if diff_func1.subs(x, val).is_real else np.nan
    for val in x_phi1
]

y_phi2 = [
    float(diff_func2.subs(x, val).evalf()) if diff_func2.subs(x, val).is_real else np.nan
    for val in x_phi2
]

plt.figure(figsize=(8, 6))
plt.title('График производных φ1 и φ2', fontsize=14, fontname='Times New Roman')

plt.plot(x_phi1, y_phi1, color="blue", label="φ1' (x)")
plt.plot(x_phi2, y_phi2, color="red", label="φ2' (x)")

plt.grid()
plt.legend()
plt.show()
