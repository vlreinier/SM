import numpy as np
import matplotlib.pyplot as plt

def tank_concentrations(steps=1000, liters=1000, inflow=6, outflow=6, concentration_inflow=0.1):
    concentrations = []
    current_concentration = 0
    current_volume = liters
    concentrations.append(current_concentration)

    for _ in range(steps):
        # Save temp volume to change tank concentration with added new volume
        temp_volume = current_volume

        # Change volume according to in and out flow
        current_volume += inflow - outflow

        # Salt concentration going into the tank with new volume
        concentration_in = concentration_inflow * inflow / current_volume

        # Salt concentration going out of the tank with new volume
        concentration_out = current_concentration * outflow / current_volume

        # New tank salt concentration for tank with new volume
        new_tank_concentration = current_concentration * temp_volume / current_volume

        # New tank salt concentration for tank after concentration in and out tank with new volume
        current_concentration = new_tank_concentration + concentration_in - concentration_out

        concentrations.append(current_concentration)
    return concentrations

concentrations_6 = tank_concentrations(outflow=6)
concentrations_5 = tank_concentrations(outflow=5)

plt.title("Salt concentration over time")
plt.plot(range(len(concentrations_6)), concentrations_6, label="6 L/min")
plt.plot(range(len(concentrations_5)), concentrations_5, label="5 L/min")
plt.yticks(np.arange(0, 0.11, step=.005))
plt.xlabel("Steps")
plt.ylabel("Salt concentration")
plt.legend()
plt.show()