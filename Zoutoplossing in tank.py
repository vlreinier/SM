import numpy as np
import matplotlib.pyplot as plt

def tank_concentrations(steps=1000, outflow=6):
    concentration_inflow = 0.1 # Inflow salt concentration for tank in KG/L
    inflow = 6 # Inflow for tank in L/MIN
    volume = 1000 # Initial tank volume for tank in L
    salt_concentration = 0 # Initial salt concentration in KG/L

    concentrations = []
    concentrations.append(salt_concentration)

    for _ in range(steps):

        # Current salt concentration in tank
        tank_con = salt_concentration * volume

        # Change tank volume according to in- and outflow
        volume += inflow - outflow

        # Salt concentration going into the tank
        con_in = concentration_inflow * inflow

        # Salt concentration going out of the tank
        con_out = salt_concentration * outflow

        # New salt concentration in tank
        salt_concentration = (tank_con + con_in - con_out) / volume

        # Add new tank concentration to list
        concentrations.append(salt_concentration)

    return concentrations

concentrations_6 = tank_concentrations()
concentrations_5 = tank_concentrations(outflow=5)

plt.title("Salt concentration over time")
plt.plot(range(len(concentrations_6)), concentrations_6, label="6 L/min")
plt.plot(range(len(concentrations_5)), concentrations_5, label="5 L/min")
plt.xticks(np.arange(0, 1000, step=50))
plt.yticks(np.arange(0, 0.11, step=.005))
plt.xlabel("Steps")
plt.ylabel("Salt concentration")
plt.legend()
plt.show()