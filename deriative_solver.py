import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#определяем переменную величину
t=np.arange(0, 10, 0.01)

#определяем функцию для системы диф. уравнений
def diff_func(z, t): #z-изменяемая величина для системы
    theta, omega = z #кортеж, указание изменяемых функций
    
    #первое уравнение системы
    dtheta_dt = omega
    #второе уравнение системы
    domega_dt = - k * omega - c * np.sin(theta)

    return dtheta_dt, domega_dt

#определяем начальные значения и параметры
theta0 = np.pi - 0.1
omega0 = 0

#начальное значение изменяемой величины системы
z0 = theta0, omega0

k = 0.25
c = 5.0

#решаем систему диф. уравнений
sol = odeint(diff_func, z0, t)

#строим решение в виде графика
plt.plot(t, sol[:, 0], 'b', label='theta(t)')

plt.legend()
plt.savefig('fig_1.png')