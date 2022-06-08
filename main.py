import numpy as np
import matplotlib .pyplot as plt

x = np.linspace(-3, 3, 10000)


def f(x):
    return 1-3*x**2


plt.plot(x, f(x))
plt.xlabel("x")
plt.ylabel("y")
plt.show()
