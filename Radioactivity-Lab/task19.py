import numpy as np 
import matplotlib.pyplot as plt 

count, time, thickness = np.loadtxt("task19.csv", delimiter = ',', unpack = True, skiprows=1)

#plt.plot(thickness,count, 'x')
#plt.xlabel("thickness/mm")
#plt.ylabel("count/total decays")
#plt.savefig("task19.png")
#plt.show()
l =[]
for i in count:
    i = np.log(i)
    l.append(i)

plt.plot(thickness,l ,'x')
plt.xlabel("thickness/mm")
plt.ylabel("ln(count)")


x = np.linspace(0,4,400)
y = []
for i in x:
    k = -3.15*i + 12.8
    y.append(k)
plt.plot(x,y, label='y = -3.15x + 12.8')
x = np.linspace(0,4,400)
y = []
for i in x:
    k = 2.35
    y.append(k)
plt.plot(x,y, label='y = 2.35')
y = []
for i in x:
    k = -1.6*i + 9.5
    y.append(k)
plt.plot(x,y, label='y = -1.6x + 9.5')

plt.legend()
plt.title("Aluminium Absorption Log Graph")
plt.savefig("task19_ln.png")
plt.show()




