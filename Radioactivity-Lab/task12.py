import numpy as np
import matplotlib.pyplot as plt

def gaussian(x,s,m):
    k = (2*np.pi)**0.5
    return (f/(s*k))*np.exp(-0.5*((x-m)/s)**2)



x = np.linspace(85,150,75)
m =120
s = 8
f = 300
plt.plot(x,gaussian(x,s,m), label = "gaussian")


s = 120**0.5
plt.plot(x,gaussian(x,s,m), label = "poisson")
plt.legend(loc = 'best')
data = np.loadtxt("radioactivity/task12real", delimiter = ',', unpack = True)

#plt.hist(data, bins = 15, label= "task1
#1")
y, binEdges = np.histogram(data, bins=20)
bincentres = 0.5*(binEdges[1:]+binEdges[:-1])
menStd = np.sqrt(y)
width = 2.5
plt.bar(bincentres, y , width=width, color = "magenta", yerr = menStd, capsize = 3)
plt.xlabel("Count rate /s-1")
plt.ylabel("Frequency")
plt.title("100 Counts/s")
plt.savefig("task12.png")
plt.show()