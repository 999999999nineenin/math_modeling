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