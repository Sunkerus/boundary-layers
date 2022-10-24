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
    A = int(1) 
    B = int(1)
    x = 1 
    def func(y, t):
        return t * math.sqrt(y)


    t = (2(1-(A+2*B*x)*pow(func(1,0),4))/3(1+A*x+B*x*x)*pow(func(1,0),3))
    y = 1.
    dt = .1
    ys, ts = [], []
    
    
    arr = np.array([0,1,-1,1],[1,0,0,1])

    while t <= 10:
        y = runge_kutta(y, t, dt, func)
        t += dt
        ys.append(y)
        ts.append(t)

    exact = [(t ** 2 + 4) ** 2 / 16. for t in ts]
    plt.plot(ts, ys, label='runge_kutta')
    plt.plot(ts, exact, label='exact')
    plt.legend()
    plt.show()
    error = np.array(exact) - np.array(ys)
    print("max error {:.5f}".format(max(error)))