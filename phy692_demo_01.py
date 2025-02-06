# Demo
import time
from phy692 import heaterExperiment
import numpy as np
import matplotlib.pyplot as plt

# Create an instance of the simulated "experiment"
h = heaterExperiment()

# Set Target temperature
temperatureTarget = 100.0
h.set_temperature_target(temperatureTarget)

# repeat the above steps until temperatureTarget reached OR timeout
t = time.time()

# start the experiment
h.start_heating()

N = 20
tempCurrent = np.zeros(N)
elapsed = np.zeros(N)

for i in range(20):
    # time.sleep(1.0) 
    while time.time() < (elapsed[i]+1):
        elapsed[i] = time.time() - t
        tempCurrent[i] = h.getCurrentTemperature()
        print("{:.3f} {:.1f}".format(elapsed[i], tempCurrent[i]))

h.stop_heating()

plt.figure()
plt.plot(elapsed, tempCurrent,'o')
plt.show()

# for i in range(10):
#     print(i)