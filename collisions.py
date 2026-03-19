import numpy as np
from scipy.integrate import odeint

def collision(x1,y1,vx1,vy1,x2,y2,vx2,vy2,radius,mass1,mass2,K):

    r12=np.sqrt((x1-x2)**2+(y1-y2)**2) #расчет расстояния между центрами частиц
    v1=np.sqrt(vx1**2+vy1**2) #расчет модулей скоростей частиц
    v2=np.sqrt(vx2**2+vy2**2)

    #проверка условия на столкновение: расстояние должно быть меньше 2-х радиусов
    if r12<=2*radius:
        if v1!=0:
            theta1 = np.arccos(vx1 / v1)
        else:
            theta1 = 0
        if v2!=0:
            theta2 = np.arccos(vx2 / v2)
        else:
            theta2 = 0
        if vy1<0:
            theta1 = - theta1 + 2 * np.pi
        if vy2<0:
            theta2 = - theta2 + 2 * np.pi

        #вычисление угла соприкосновения
        if (y1-y2)<0:
            phi = - np.arccos((x1-x2) / r12) + 2 * np.pi
        else:
            phi = np.arccos((x1-x2) / r12)

        # Пересчет  x-компоненты скорости первой частицы
        VX1 = v1 * np.cos(theta1 - phi) * (mass1 - K * mass2) \
        * np.cos(phi) / (mass1 + mass2)\
        + ((1 + K) * mass2 * v2 * np.cos(theta2 - phi))\
        * np.cos(phi) / (mass1 + mass2)\
        + K * v1 * np.sin(theta1 - phi) * np.cos(phi + np.pi / 2)

        # Пересчет y-компоненты скорости первой частицы
        VY1 = v1 * np.cos(theta1 - phi) * (mass1 - K * mass2) \
        * np.sin(phi) / (mass1 + mass2) \
        + ((1 + K) * mass2 * v2 * np.cos(theta2 - phi)) \
        * np.sin(phi) / (mass1 + mass2) \
        + K * v1 * np.sin(theta1 - phi) * np.sin(phi + np.pi / 2)

        # Пересчет x-компоненты скорости второй частицы
        VX2 = v2 * np.cos(theta2 - phi) * (mass2 - K * mass1) \
        * np.cos(phi) / (mass1 + mass2)\
        + ((1 + K) * mass1 * v1 * np.cos(theta1 - phi)) \
        * np.cos(phi) / (mass1 + mass2)\
        + K * v2 * np.sin(theta2 - phi) * np.cos(phi + np.pi / 2)

        # Пересчет y-компоненты скорости второй частицы
        VY2 = v2 * np.cos(theta2 - phi) * (mass2 - K * mass1) \
        * np.sin(phi) / (mass1 + mass2) \
        + ((1 + K) * mass1 * v1 * np.cos(theta1 - phi)) \
        * np.sin(phi) / (mass1 + mass2)\
        + K * v2 * np.sin(theta2 - phi) * np.sin(phi + np.pi / 2)

    else:
        #если условие столкновнеия не выполнено, то скорости частиц не пересчитываются
        VX1, VY1, VX2, VY2 = vx1, vy1, vx2, vy2

    return VX1, VY1, VX2, VY2

def discretizator(move_func,T1,T2,N,ics,params):
    tau=np.linspace(T1,T2,N)
    x1,x2,y1,y2 = [],[],[],[]
    x10,v_x10,y10,v_y10,x20,v_x20,y20,v_y20 = ics[0],ics[1],ics[2],ics[3],ics[4],ics[5],ics[6],ics[7]
    x1.append(x10)
    y1.append(y10)
    x2.append(x20)
    y2.append(y20)
    radius,mass1,mass2,K = params[0],params[1],params[2],params[3]
    for k in range(N-1):
        t=[tau[k],tau[k+1]]
        s0 = x10,v_x10,y10,v_y10,x20,v_x20,y20,v_y20
        sol = odeint(move_func, s0, t)
        #новые начальные условия для следующей итерации
        x10=sol[1,0]
        x1.append(x10)
        v_x10=sol[1,1]
        y10=sol[1,2]
        y1.append(y10)
        v_y10=sol[1,3]
        x20=sol[1,4]
        x2.append(x20)
        v_x20=sol[1,5]
        y20=sol[1,6]
        y2.append(y20)
        v_y20=sol[1,7]
        r1=np.sqrt((x1[k]-x2[k])**2+(y1[k]-y2[k])**2)
        r0=np.sqrt((x1[k-1]-x2[k-1])**2+(y1[k-1]-y2[k-1])**2)
        if np.absolute(r1<=radius*2 and r0>radius*2):
            res=collision(x10,y10,v_x10,v_y10,x20,y20,v_x20,v_y20,radius,mass1,mass2,K)
            v_x10,v_y10=res[0],res[1]
            v_x20,v_y20=res[2], res[3]
    return x1, x2, y1, y2

def collision_with_walls(x1, y1, vx1, vy1, Lx, Ly, radius, K1):
    if (x1 <= (- Lx + radius) or x1 >= (Lx - radius)):
        VX = - K1 * vx1
    else:
        VX = vx1
    if (y1 <= (- Ly + radius) or y1 >= (Ly - radius)):
        VY = - K1 * vy1
    else:
        VY = vy1
    return VX, VY

def circle_func(x_centre_point, # х-координата центральной точки окружности
                y_centre_point, # у-координата центральной точки окружности
                R):
    x = np.zeros(30) #Создание массива для координаты х
    y = np.zeros(30) #Создание массива для координаты у
    for i in range(0, 30, 1): # Цикл, определяющий множество точек окружности относительно центра
        alpha = np.linspace(0, 2*np.pi, 30)
        x[i] = x_centre_point + R*np.cos(alpha[i])
        y[i] = y_centre_point + R*np.sin(alpha[i])

    return x, y