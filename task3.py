import numpy as np
from constans import g 

x0 = 0
y0 = 0 
alpha = 30 * (np.pi / 180)
V = 1
Vx0 = V * np.cos(alpha)
Vy0 = V * np.sin(alpha)

t = np.linspace(0 , 20 , 0.01)
x = x0 + Vx0 * t
y = y0 + Vy0 * t

coords = np.zeros((3 , len(t)))
coords[: , 0 ] = t[:]
coords[: , 1] = x[:]
