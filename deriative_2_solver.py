import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x=np.arange(1, 3, 0.01)

def diff_func(z, x): 
    y, omega = z 

    dy_dx = omega

    domega_dx = np.sin(y) * omega - 3*x*y - 5
    return dy_dx, domega_dx

y0 = 0.01
omega0 = 0.05

z0 = y0, omega0

sol = odeint(diff_func, z0, x)

plt.plot(x, sol[:, 0], 'b', label='y(x)')
plt.plot(x, sol[:, 1], 'g', label='omega(x)')

plt.legend()
plt.savefig('fig_2.png')