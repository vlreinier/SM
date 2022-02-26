import math
import matplotlib.pylab as plt
import numpy as np


def euler_heun(steps=100):
    euler = np.zeros([steps + 1])
    heun = np.zeros([steps + 1])
    e = np.zeros([steps + 1])

    h = 1 / steps
    t = list(np.arange(0, 1+h, step=h))

    heun[0] = 1
    euler[0] = 1
    e[0] = math.e ** 0

    for step in range(steps):
        euler[step + 1] = euler[step] + h * euler[step]  # Euler
        heun[step + 1] = heun[step] + h * ((euler[step] + euler[step + 1])/2)  # Heun
        e[step + 1] = math.e ** t[step]  # e^t

    return t, euler, heun, e

fig, axes = plt.subplots(nrows=1, ncols=2)

for x in [5, 10, 20, 100]:
    t, euler, heun, e = euler_heun(steps=x)

    # Euler
    axes[0].title.set_text("Euler")
    axes[0].plot(t, euler, label="n = {}".format(x))
    axes[0].axhline(y=math.e, color='black', linestyle='--')
    axes[0].legend()

    # Heun
    axes[1].title.set_text("Heun")
    axes[1].plot(t, heun, label="n = {}".format(x))
    axes[1].axhline(y=math.e, color='black', linestyle='--')
    axes[1].legend()

plt.tight_layout()
plt.show()