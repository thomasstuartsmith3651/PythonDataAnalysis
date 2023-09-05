import numpy as np 
import matplotlib.pyplot as plt 

count, time, thickness = np.loadtxt("task20.csv", delimiter = ',', unpack = True, skiprows=1)

#plt.plot(thickness,count, 'x')
#plt.xlabel("thickness/mm")
#plt.ylabel("count/total decays")
#plt.savefig("task20.png")
#plt.show()
l =[]
for i in count:
    i = np.log(i)
    l.append(i)

plt.plot(thickness,l ,'x')
plt.xlabel("thickness/mm")
plt.ylabel("ln(count)")
plt.title("Copper Absorption Log Graph")

x = np.linspace(0,1,400)
y = []
for i in x:
    k = -8.96*i +10.8
    y.append(k)
plt.plot(x,y,label='y = -8.96x + 10.8')
x = np.linspace(0,1,400)
y = []
for i in x:
    k = -5.9*i +9.33
    y.append(k)
plt.plot(x,y,label='y = -5.9x + 9.33')
x = np.linspace(0,1.4,400)
y = []
for i in x:
    k = -2.8*i + 5.1
    y.append(k)
plt.plot(x,y,label='y = -2.8x + 5.1')
plt.legend()
plt.savefig("task20_ln.png")

plt.show()
