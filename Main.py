import math
import numpy as np
import matplotlib.pyplot as plt

def runge_kutta(y, x, dx, f):
    k1 = dx * f(y, t)
    k2 = dx * f(y + 0.5 * k1, x + 0.5 * dx)
    k3 = dx * f(y + 0.5 * k2, x + 0.5 * dx)
    k4 = dx * f(y + k3, x + dx)
    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6.

if __name__=='__main__':
    t = 0.
    y = 0.719
    dt = .1
    ys, ts = [], []
def func(y, t):
    A = 1
    B = 1
    return  (2*(1-(A+2*B*t))*y**4)/(3*(1+A*t+B*(t**2))*y**3)


while t <= 1:
    y = runge_kutta(y, t, dt, func)
    t += dt
    ys.append(y)
    ts.append(t)
    print("y =", y ,"\t")
    print("dx = ", t ,"\t")
   

exact = [pow(8/3*t,1/4) for t in ts]
print("exact =", exact, "\t")
print("\n")
plt.plot(ts, ys, label='runge_kutta')
plt.plot(ts, exact, label='exact')
plt.legend()
plt.show()
error = np.array(exact) - np.array(ys)
print("max error {:.5f}".format(max(error)))