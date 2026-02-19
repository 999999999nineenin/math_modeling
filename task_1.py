import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)

def diff_func(s, x):
    y, z = s

    dy_dx = y**2*z

    dz_dx = z / (x + 0.01) -y*z**2

    return dy_dx, dz_dx

y0 = 1
z0 = -3

s0 = y0, z0

sol=odeint(diff_func, s0, x)

plt.plot(x, sol[:, 0], 'b', label='x(y)')
plt.plot(x, sol[:, 1], 'g', label='x(z)')

plt.legend()
plt.savefig('fig_3.png')