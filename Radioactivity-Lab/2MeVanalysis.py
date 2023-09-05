import numpy as np
import matplotlib.pyplot as plt
import math as math
import random
def gaussian(x,s,m):
    k = (2*np.pi)**0.5
    return (f/(s*k))*np.exp(-0.5*((x-m)/s)**2)

x = np.arange(-0.4,0.22,0.02)
m =0
s = 0.12
f = 22




data = np.loadtxt("2MeVdata.csv",delimiter = ',',skiprows=1)
distance = []
frequency = []
for i in range(len(data)):
    frequency.append(data[i,2])
    while frequency[i] > 0:
        distance.append(data[i,0])
        frequency[i] = frequency[i] - 1
angle=[]
for i in distance:
    i = int(i)
    distance[i] = distance[i] -2.5
    angle.append(math.atan(distance[i]/30)-0.783)



y, binEdges = np.histogram(angle, bins=13)
bincentres = 0.5*(binEdges[1:]+binEdges[:-1])
menStd = y/10
width = 0.0475
plt.bar(bincentres, y , width=width, color = "magenta", yerr = menStd, capsize = 3)
plt.xlabel("Angle (rad)")
plt.ylabel("Frequency")
plt.title("2MeV Scattering Angle Distribution")


plt.plot(x,gaussian(x,s,m), label = "gaussian")
plt.savefig("2MeVScatAngDist.png")
plt.show()
