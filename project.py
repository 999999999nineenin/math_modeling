import numpy as np

def collision(x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3, x4, y4, vx4, vy4, x5, y5, vx5, vy5, x6, y6, vx6, vy6, x7, y7, vx7, vy7, x8, y8, vx8, vy8, x9, y9, vx9, vy9, x10, y10, vx10, vy10, x11, y11, vx11, vy11, x12, y12, vx12, vy12, x13, y13, vx13, vy13, x14, y14, vx14, vy14, x15, y15, vx15, vy15, x16, y16, vx16, vy16, radius, mass):

    r1_2 = np.sqrt((x1-x2)**2), np.sqrt((y1-y2)**2) # Расчет расстояния между центрами частиц
    r1_3 = np.sqrt((x1-x3)**2), np.sqrt((y1-y3)**2)
    r1_4 = np.sqrt((x1-x4)**2), np.sqrt((y1-y4)**2)
    r1_5 = np.sqrt((x1-x5)**2), np.sqrt((y1-y5)**2)
    r1_6 = np.sqrt((x1-x6)**2), np.sqrt((y1-y6)**2)
    r1_7 = np.sqrt((x1-x7)**2), np.sqrt((y1-y7)**2)
    r1_8 = np.sqrt((x1-x8)**2), np.sqrt((y1-y8)**2)
    r1_9 = np.sqrt((x1-x9)**2), np.sqrt((y1-y9)**2)
    r1_10 = np.sqrt((x1-x10)**2), np.sqrt((y1-y10)**2)
    r1_11 = np.sqrt((x1-x11)**2), np.sqrt((y1-y11)**2)
    r1_12 = np.sqrt((x1-x12)**2), np.sqrt((y1-y12)**2)
    r1_13 = np.sqrt((x1-x13)**2), np.sqrt((y1-y13)**2)
    r1_14 = np.sqrt((x1-x14)**2), np.sqrt((y1-y14)**2)
    r1_15 = np.sqrt((x1-x15)**2), np.sqrt((y1-y15)**2)
    r1_16 = np.sqrt((x1-x16)**2), np.sqrt((y1-y16)**2)

    # Проверка условия на столкновение: расстояние
    # должно быть меньше 2-х радиусов
    if r1_2 <= 2*radius:
        # Пересчет  скорости первой частицы
        VX1 = vx1 * mass / mass + (2) * mass * vx2 / mass

        # Пересчет скорости второй частицы
        VX2 = vx2 * mass / mass + (2) * mass * vx1 / mass

    else:
        # Eсли условие столкновнеия не выполнено,
        # то скорости частиц не пересчитываются
        VX1, VY1, VX2, VY2, VX3, VY3, VX4, VY4, VX5, VY5, VX6, VY6, VX7, VY7, VX8, VY8, VX9, VY9, VX10, VY10, VX11, VY11, VX12, VY12, VX13, VY13, VX14, VY14, VX15, VY15, VX16, VY16 = vx1, vy1, vx2, vy2, vx3, vy3, vx4, vy4, vx5, vy5, vx6, vy6, vx7, vy7, vx8, vy8, x9, y9, vx9, vy9, vx10, vy10, x11, y11, vx11, vx12, x13, y13, vx13, vy13, x14, y14, vx14, vy14, x15, y15, vx15, vy15, x16, y16, vx16, vy16

    return VX1, VY1, VX2, VY2, VX3, VY3, VX4, VY4, VX5, VY5, VX6, VY6, VX7, VY7, VX8, VY8, VX9, VY9, VX10, VY10, VX11, VY11, VX12, VY12, VX13, VY13, VX14, VY14, VX15, VY15, VX16, VY16