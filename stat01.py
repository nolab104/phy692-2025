# Using this program, we will attempt to understand some essential statistics:
# means, deviations, standard errors and all that. 

import numpy as np 
import matplotlib.pyplot as plt

rng = np.random.default_rng()
L = 1 # meters
g = 9.8 # meters/sec^2
T0 = 2*np.pi*np.sqrt(L/g)

nDataPoints = np.linspace(10,10000,100, dtype = int) # number of data points recorded in each trial
# nDataPoints = np.array([10,50, 100, 500, 1000], dtype = int) # number of data points recorded in each trial
numberOfTrials = 100 # number of trials 

# Initialize arrays to store data
TDev = np.zeros([len(nDataPoints), numberOfTrials])
TDevSTD = np.zeros(len(nDataPoints))
TSTD = np.zeros(numberOfTrials)
TSTDavg = np.zeros(len(nDataPoints))

for i, N in enumerate(nDataPoints):
    # we will try to observe how the distribution of observed means is distributed around the actual value
    for j in range(numberOfTrials):
        # T = rng.normal(loc = T0, scale=T0/8, size = N) # draw N values
        T= rng.random(N)
        TAvg = np.mean(T) # average of the N values
        TSTD[j] = np.std(T) # St. Dev. of the N values
        TDev[i,j] = TAvg - T0 # deviation of this mean from the actual value
    TDevSTD[i] = np.std(TDev[i,:]) 
    TSTDavg[i] = np.mean(TSTD) # average of the sample St. dev. for a certain number of data samples.

plt.figure()
plt.subplot(1,2,1)
plt.hist(TDev[i,:])
plt.subplot(1,2,2)
# plt.plot(nDataPoints, 1/TDevSTD**2,'s')
plt.plot(nDataPoints, TSTDavg,'s')
plt.plot(nDataPoints, TDevSTD,'s')
plt.show()


