
import numpy as np
import matplotlib.pyplot as plt
import numba


def J(x, y):
    c = -.4 + .6j
    z = x + y*1j
    z = z*z + c
    return z.real, z.imag

def H(x, y):
    a = 1.4
    b = 0.3
    return 1 - a*x*x + y, b*x

F = J

def aod(x, y, n):
    D = 0
    for i in range(n):
        xn, yn = F(x, y)
        d = np.sqrt((x-xn)**2 + (y-yn)**2)
        D += d
        x, y = xn, yn
    return 1 / (n-1) * D

@numba.jit(nopython=True)
def aod2(x, y, n):
    c = -.4 + .6j
    D = 0
    for i in range(n):
        z = x + y*1j
        z = z*z + c
        xn, yn = z.real, z.imag
        d = np.sqrt((x-xn)**2 + (y-yn)**2)
        D += d
        x, y = xn, yn
    return 1 / (n-1) * D

s = np.linspace(-4, 4, 100)
s = np.linspace(-1.5, 1.5, 4000)
out = np.zeros((len(s), len(s)))

for i, ii in enumerate(s):
    for j, jj in enumerate(s):
        k = aod2(ii, jj, 20)
        out[i, j] = np.log(k)

plt.imshow(out, extent=[min(s), max(s), min(s), max(s)])
plt.colorbar()
plt.show()
