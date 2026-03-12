import numpy as np
from scipy.integrate import odeint
import matplotlib as plt
from matplotlib.animation import FuncAnimation

def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3) = s
    
    dxdt1 = v_x1
    dv_xdt1 = (k * q1 * q2 / m1 * (x1 - x2) / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 1.5
               + k * q1 * q3 / m1 * (x1 - x3) / ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 1.5)

    dydt1 = v_y1
    dv_ydt1 = (k * q1 * q2 / m1 * (y1 - y2) / ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 1.5
               + k * q1 * q3 / m1 * (y1 - y3) / ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 1.5)

    dxdt2 = v_x2
    dv_xdt2 = (k * q2 * q1 / m2 * (x2 - x1) / ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 1.5
               + k * q2 * q3 / m2 * (x2 - x3) / ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 1.5)

    dydt2 = v_y2
    dv_ydt2 = (k * q2 * q1 / m2 * (y2 - y1) / ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 1.5
               + k * q2 * q3 / m2 * (y2 - y3) / ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 1.5)

    dxdt3 = v_x3
    dv_xdt3 = (k * q3 * q1 / m3 * (x3 - x1) / ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 1.5
               + k * q3 * q2 / m3 * (x3 - x2) / ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 1.5)

    dydt3 = v_y3
    dv_ydt3 = (k * q3 * q1 / m3 * (y3 - y1) / ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 1.5
               + k * q3 * q2 / m3 * (y3 - y2) / ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 1.5)

    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3)

def animate (i):
    for j in range(3):
        balls[j][0].set_data([sol[i, 4 * j]], [sol[i, 4 * j+2]])
        ball_lines[j][0].set_data([sol[:i, 4 * j]], [sol[:i, 4 * j+2]])

frames = 365
seconds_in_year = 365 * 24 * 60 * 60
years = 0.5
t = np.linspace(0, years * seconds_in_year, frames)

a_e = 149 * 10 ** 9

x1 = 0
v_x1 = 0
y1 = a_e * np.sqrt(0.75)
v_y1 = 0

x2 = a_e / 2
v_x2 = 10000
y2 = 0
v_y2 = 0

x3 = a_e / 2
v_x3 = -10000
y3 = 0
v_y3 = 0

s0 = (x1, v_x1, y1, v_y1,
      x2, v_x2, y2, v_y2,
      x3, v_x3, y3, v_y3)

m1, m2, m3 = 1
q = 2 * 10 ** 5

q1, q2, q3 = -q, q, q
k = 8.98755 * 10 ** 9 

sol = odeint(move_func, s0, t)

fig, ax = plt.subplots()

balls = []
balls_lines = []

for i in range(3):
    balls.append(plt.plot([], [], 'o', color='r'))
    balls_lines.append(plt.plot([], [], '-', color='r'))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

plt.axis('equal')
edge = 2 * x1
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('N_body_anim.gif', writer='pillow')