import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import moyal



data =  np.loadtxt('data_beta_2MeV_15000.txt', skiprows = 1, delimiter=',')
val = []
pal = []
for i in range(len(data)):
    if data[i,0] < 400:
        val.append(data[i,0])
    else:
        pal.append(data[i,0])
    

print(pal)
np.savetxt('2MeV.txt',val)

plt.hist(val,bins=100)
x = np.linspace(-87, 400, 1000)
y = moyal.pdf(x,0,8.2)
for i in range(len(y)):
    y[i]=45000*y[i]

plt.xlabel('Energy Deposited (keV)')
plt.ylabel('Frequency')
plt.title('Landau Approximation Fit, 2MeV')
plt.plot((x+84),y, 'r-', lw=2, alpha=0.6, label='moyal pdf')
plt.savefig('LandauApproximation.png')
plt.show()