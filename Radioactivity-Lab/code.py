import numpy as np
import matplotlib.pyplot as plt

triggered = []
time_trig = []
trigger = 0.03

time, value = np.loadtxt("./CSVs/WFM17.csv", delimiter = ',', unpack = True, skiprows = 1)

for i in range(len(time)):
    if value[i] > trigger:
        triggered.append(value[i])
        time_trig.append(time[i])

plt.plot(time,value)
plt.scatter(time_trig,triggered)
plt.show()

print(triggered)

#np.savetxt("WFM17.txt", triggered, delimiter = ',')

