from sympy import *
from sympy.plotting import plot3d

x, y = symbols("x y")
g = 2 * x**3 + 3 * y**3
plot3d(g)

show()
