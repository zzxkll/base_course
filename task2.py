import numpy as np
from numpy import sqrt 
from constans import k , g , e
h = 100 
a = 45
b = 35


V = sqrt((g* h * np.tan(b)**2)/(2 * np.cos(a)**2 * (1- np.tan(b) * np.tan(a) )))

print('V =' , V)

T = 200
e1 = 300

N = (2 / sqrt(np.pi)) * (h/ (k * T)**(3/2)) * e**(-e1/k*T) * e1**(T/2)

print('N =', N)