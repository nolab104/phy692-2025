# Useful set of programs for PHY692
import time
import numpy as np

# A simple program to mimic a tumbler of water heating to 50 deg. C.
class heaterExperiment:
    def __init__(self, tempTarget = 50.0, rate=1.0, tempInit = 20.0, timeOut = 60.0):  
        self.rate = rate # degree Celsius per second
        self.tempStart = tempInit # initial temperature deg. C.
        self.timeStart = 0 # time in seconds
        self.timeStop = timeOut
        self.noiseSigma = 0.5
        self.tempTarget = tempTarget
        self.rng = np.random.default_rng()

    def set_rate(self, r):  # degree Celsius per second
        self.rate = r

    def set_temperature_target(self, T):  # degree Celsius per second
        self.tempTarget = T
    
    def start_heating(self):
        self.timeStart = time.time()

    def stop_heating(self):
        self.timeStop = time.time()

    def getCurrentTemperature(self):
        timeElapsed = time.time - self.timeStart
        tempCurrent = np.max([self.tempStart + self.rate*np.min(timeElapsed, self.timeStop), self.tempTarget]) + self.rng.normal(0.0, self.noiseSigma)
        return tempCurrent

