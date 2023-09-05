import numpy as np
import matplotlib.pyplot as plt

def poisson(x,l):
    h = []
    for i in x:
        i = int(i)
        h.append((s*l**i*np.exp(-1 * l))/np.math.factorial(i))
    return h
s = 260
l=9.7
x = np.linspace(0,20,20)

plt.plot(x,poisson(x,l))

data = np.loadtxt("radioactivity/task11real", delimiter = ',', unpack = True)
y, binEdges = np.histogram(data, bins=10)
bincentres = 0.5*(binEdges[1:]+binEdges[:-1])
menStd = np.sqrt(y)
width = 2
print(binEdges)
#plt.hist(data, bins = 10, label= "task11")
plt.bar(bincentres, y , width=width, color = "magenta", yerr = menStd, capsize = 3)
plt.xlabel("Count rate /s-1")
plt.ylabel("Frequency")
plt.title("7-10 Counts/s")
plt.savefig("task11.png")
plt.show()