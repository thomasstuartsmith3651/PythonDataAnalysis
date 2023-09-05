import numpy as np
import matplotlib.pyplot as plt

data, a, b, c = np.loadtxt("data_beta_2MeV_15000.txt", unpack=True, skiprows=1, delimiter=',')
data1, a1, b1, c1 = np.loadtxt("data_beta_300keV_15000.txt", unpack=True, skiprows=1, delimiter=',')

#data2 = np.concatenate((data, data1), axis = None)

plt.hist(data,bins=2000, label = '2MeV')
plt.hist(data1,bins=2000, label = '300keV')
plt.xlabel("Energy Deposited /keV")
plt.ylabel("Frequency")
#plt.hist(data2, bins=2000)
plt.title("Energy Deposited by Particles In the Detector")

plt.legend(loc = 'best')

plt.savefig("task7.png", dpi = 300)

plt.show()




#data2, a2, b2, c2 = np.loadtxt("data_lots.txt", unpack=True, skiprows=1, delimiter=',')

#plt.hist(data2, bins=50)

#plt.show()