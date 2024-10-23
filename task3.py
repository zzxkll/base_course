import numpy as np
from numpy import sqrt 
h = 100 
a = 45
b = 35
g = 9.80665

V = sqrt((g* h * np.tan(b)**2)/(2 * np.cos(a)**2 * (1- np.tan(b) * np.tan(a) )))

print(V)

T = 200

N = (2 / sqrt(np.pi)) * (h/ (k * T)**(3/2))