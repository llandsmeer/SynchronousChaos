import numpy as np
import matplotlib.pyplot as plt

s = np.linspace(-2, 2, 1000)
x, y = np.meshgrid(s, s)
c = x + y*1j
z = 0

out = np.zeros_like(c, dtype=int)

for i in range(500):
    z = z**2 + c
    out += np.absolute(z) < 1

plt.imshow(np.log(out+1))
plt.colorbar()
plt.show()

def nd_orbit(f, x0, n):
    x = x0
    xs = []
    for i in range(n):
        x = f(x)
        xs.append(x)
    return np.array(xs)

