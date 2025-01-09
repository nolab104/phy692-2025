# Demo
import time
from phy692 import heaterExperiment

# Create an instance of the simulated "experiment"
h = heaterExperiment

# Set Target temperature
temperatureTarget = 100
h.set_temperature_target(temperatureTarget)

# repeat the above steps until temperatureTarget reached OR timeout
t = time.time()
# do stuff

while (tempCurrent < temperatureTarget):
    #tempCurrent = getTemperature()
    elapsed = time.time() - t
    tempCurrent = tempCurrent + 1
    time.sleep(0.1)
    print(elapsed, tempCurrent)

# for i in range(10):
#     print(i)