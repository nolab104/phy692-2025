# Demo
import time
from phy692 import heaterExperiment

# Create an instance of the simulated "experiment"
h = heaterExperiment()

# Set Target temperature
temperatureTarget = 100.0
h.set_temperature_target(temperatureTarget)

# repeat the above steps until temperatureTarget reached OR timeout
t = time.time()

# start the experiment
h.start_heating()

for i in range(5):
    time.sleep(1.0)
    elapsed = time.time() - t
    tempCurrent = h.getCurrentTemperature()
    print(elapsed, tempCurrent)

h.stop_heating()
# for i in range(10):
#     print(i)