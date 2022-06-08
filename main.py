import numpy as np
import matplotlib.pyplot as plt


def henon_attractor(x, y, a=.1, b=0.03):
    '''Computes the next step in the Henon
    map for arguments x, y with kwargs a and
    b as constants.
    '''
    dx = 1 - a * x ** 2 + y
    dy = b * x
    return dx, dy


# number of iterations and step size
steps = 5000000
delta_t = 0.0047

X = np.zeros(steps + 1)
Y = np.zeros(steps + 1)

# starting point
X[0], Y[0] = 1, 0

# compute using Euler's formula
for i in range(steps):
    x_dot, y_dot = henon_attractor(X[i], Y[i])
    X[i + 1] = X[i] + x_dot * delta_t
    Y[i + 1] = Y[i] + y_dot * delta_t

# display plot
plt.plot(Y, X, ls='', marker=',', alpha=0.1, markersize=0.1)
plt.axis('on')
plt.show()
