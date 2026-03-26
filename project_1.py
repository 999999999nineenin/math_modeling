import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames=10000

def collision_with_walls(x1, y1, vx1, vy1, Lx, Ly, radius, K1=1):
    if (x1 <= (- Lx + radius) or x1 >= (Lx - radius)):
        VX = - K1 * vx1
    else:
        VX = vx1
    if (y1 <= (- Ly + radius) or y1 >= (Ly - radius)):
        VY = - K1 * vy1
    else:
        VY = vy1
    return VX, VY

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='b')
ball_line, = plt.plot([], [], '-', color='b')
plt.plot([0], [0], 'o', color='y', ms=20)


def animate(i):
    ball.set_data(collision_with_walls(i, 'point'))
    ball_line.set_data(collision_with_walls(i, 'line'))


ani = FuncAnimation(fig, animate, frames=frames, interval=30)

plt.axis('equal')
edge = 2 * Lx
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('earth_sun.gif')