import numpy as np
import matplotlib.pyplot as plt

def tank_concentrations(steps=120, liters=1000, inflow=6, outflow=6, concentration_inflow=0.1):
    concentrations = []
    current_concentration = 0
    concentrations.append(current_concentration)
    for step in range(steps):
        in_tank = inflow / liters * concentration_inflow # salt concentration in flow for this step
        out_tank = outflow / liters * current_concentration # salt concentration out flow for this step
        current_concentration = current_concentration + in_tank - out_tank
        concentrations.append(current_concentration)
    return concentrations

fig, axes = plt.subplots(nrows=1, ncols=2)

# Outflow 6
concentrations_6 = tank_concentrations(outflow=6)
axes[0].title.set_text("Tank outflow: 6 L/min")
axes[0].plot(range(len(concentrations_6)), concentrations_6)
axes[0].set_yticks(np.arange(0, 0.06, step=.005))
axes[0].set_xlabel("Steps")
axes[0].set_ylabel("Salt concentration")

# Outflow 5 -> salt concentration in tank remains higher since in and outflow are not identical
concentrations_5 = tank_concentrations(outflow=5)
axes[1].title.set_text("Tank outflow: 5 L/min")
axes[1].plot(range(len(concentrations_5)), concentrations_5)
axes[1].set_yticks(np.arange(0, 0.06, step=.005))
axes[1].set_xlabel("Steps")
axes[1].set_ylabel("Salt concentration")

plt.tight_layout()
plt.show()