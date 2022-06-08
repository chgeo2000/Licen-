import numpy as np
import matplotlib.pyplot as plt


def henon_attractor(x, y, a=1.4, b=0.3):
    '''Computes the next step in the Henon
    map for arguments x, y with kwargs a and
    b as constants.
    '''
    x_next = 1 - a * x ** 2 + y
    y_next = b * x
    return x_next, y_next


# number of iterations and array initialization
steps = 100000
X = np.zeros(steps + 1)
Y = np.zeros(steps + 1)
X_second = np.zeros(steps + 1)
Y_second = np.zeros(steps + 1)
X_third = np.zeros(steps + 1)
Y_third = np.zeros(steps + 1)
X_fourth = np.zeros(steps + 1)
Y_fourth = np.zeros(steps + 1)


# starting point
X[0], Y[0] = 0, 0
X_second[0], Y_second[0] = 0, 0
X_third[0], Y_third[0] = 0, 0
X_fourth[0], Y_fourth[0] = 0, 0

# add points to array
for i in range(steps):
    x_next, y_next = henon_attractor(X[i], Y[i])

    x_second = x_next
    y_second = 1 - 1.4 * x_next**2 + y_next

    x_third = 0.3 * x_second
    y_third = y_next

    x_fourth = y_third
    y_fourth = x_third

    X[i + 1] = x_next
    Y[i + 1] = y_next
    X_second[i + 1] = x_second
    Y_second[i + 1] = y_second
    X_third[i + 1] = x_third
    Y_third[i + 1] = y_third
    X_fourth[i + 1] = x_fourth
    Y_fourth[i + 1] = y_fourth


plt.plot(X_third, Y_third, '^', color='blue', alpha=0.8, markersize=0.3)
plt.xlabel("x'''")
plt.ylabel("y'''")
plt.show()

