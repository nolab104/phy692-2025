import numpy as np 
import matplotlib.pyplot as plt


x = np.linspace(-2,2, 512)
y = np.sinc(x)

for i in [1,2,3,4,5,10]:
    plt.plot(x,y**i, label = "{:d}".format(i))
plt.legend()
plt.show()