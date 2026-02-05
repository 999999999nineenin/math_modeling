import sympy as sym
from sympy.vector import CoordSys3D

N = CoordSys3D('N')
a, b, c = sym.symbols('a b c')

v = N.i - 2*N.j
print(v/3)
print(v*4/3)

v1 = 2*N.i + 3*N.j - N.k
v2 = N.i - 4*N.j + N.k

sol = v1.dot(v2)#скалярное произведение векторов
print(sol)

sol = v1.cross(v2)#векторное произведение векторов
print(sol)
