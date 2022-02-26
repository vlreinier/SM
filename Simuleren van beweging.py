import numpy as np
import matplotlib.pyplot as plt

def forward_euler():
    h = 0.1 # s
    g = 9.81 # m / s2

    num_steps = 50

    t = np.zeros(num_steps + 1)
    x = np.zeros(num_steps + 1)
    v = np.zeros(num_steps + 1)

    for step in range(num_steps):
        t[step + 1] = t[step] + h
        x[step + 1] = x[step] + (h * v[step]) # h == (t[step + 1] - t[step])
        v[step + 1] = v[step] - (h * g) # h == (t[step + 1] - t[step])
    return t, x, v

t, x, v = forward_euler()
print(v)
axes_height = plt.subplot(211)
plt.plot(t, x)
axes_velocity = plt.subplot(212)
plt.plot(t, v)
axes_height.set_ylabel("Height in m")
axes_velocity.set_ylabel("Velocity in m/s2")
axes_velocity.set_xlabel("Time in s")
plt.show()