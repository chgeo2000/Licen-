import matplotlib .pyplot as plt
import numpy as np

R = np.linspace(2.8, 4.0, 100000)

X = []
Y = []


for r in R:
    X.append(r)

    x = np.random.random()
    for n in range(100):
        x = r * x * (1-x)

    for n in range(100):
        x = r * x * (1 - x)

    Y.append(x)

plt.plot(X, Y, ls='', marker=',')
plt.show()
