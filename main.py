import numpy as np
from matplotlib import pyplot as plt
from math import pi

u = 1     # x-position of the center
v = 0.5    # y-position of the center
a = 2     # radius on the x-axis
b = 1.5    # radius on the y-axis

t = np.linspace(0, 2*pi, 80)

plt.plot(u+a*np.cos(t), v+b*np.sin(t), color='blue', alpha=1, markersize=0.9)

plt.xlabel("x")
plt.ylabel("y")

plt.show()
