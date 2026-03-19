import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

# Решение задачи на динамику электрона в электромагнитном поле

# Определяем переменную величину
t = np.linspace(0, 4, 4000)

# Определяем функцию для системы диф. уравнений
def move_func(s, t):
    x, v_x, y, v_y, z, v_z = s

    # Поле магнитного диполя при его ориентации вдоль оси
    Bx = 3 * x * z * mu_d * mu / (x**2 + y**2 + z**2)**(5/2)
    By = (3 * y * z * mu_d) * mu / (x**2 + y**2 + z**2)**(5/2)
    Bz = (2 * z**2 - x**2 - y**2)* mu_d * mu / (x**2 + y**2 + z**2)**(5/2)

    dxdt = v_x
    dv_xdt = q / m * (v_y * Bz - By * v_z)

    dydt = v_y
    dv_ydt = q / m * (v_z * Bx - Bz * v_x)

    dzdt = v_z
    dv_zdt = q / m * (v_x * By - Bx * v_y)

    return dxdt, dv_xdt, dydt, dv_ydt, dzdt, dv_zdt

# Определяем начальные значения и параметры
x0 = 10
v_x0 = 0

y0 = 10
v_y0 = 0

z0 = 10
v_z0 = - 10**3

s0 = x0, v_x0, y0, v_y0, z0, v_z0

q = 1.6 * 10**(-19) # Модуль заряда электрона
m = 9.1 * 10**(-31) # Масса электрона
mu = 1.26 * 10**(-6) # Магнитная постоянная
mu_d = 2 * 10**2 # Магнитный момент диполя

edge = 15

# Решаем систему диф. уравнений
sol = odeint(move_func, s0, t)

# Строим решение в виде графика
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.plot(sol[:, 0], sol[:, 2], sol[:, 4], label='electron trajectory')

# Украшательсвта и масштабирование
ax.set_xlim3d([-edge, edge])
ax.set_xlabel('X')

ax.set_ylim3d([-edge, edge])
ax.set_ylabel('Y')

ax.set_zlim3d([-edge, edge])
ax.set_zlabel('Z')

plt.show()

plt.savefig('999999999.png')