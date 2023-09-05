import numpy as np 
import matplotlib.pyplot as plt 

yellowAmp2,yellowPos2 = np.loadtxt('Hg_Yellow_Fast2.txt',unpack = 'true', usecols = (1,5))
yellowAmp1,yellowPos1 = np.loadtxt('Hg_Yellow_Fast2.txt',unpack = 'true', usecols = (1,5))



plt.plot(yellowPos2,yellowAmp2,'-b')
plt.title('Yellow Doublet 2')
plt.xlabel('Position(µSteps)')
plt.ylabel('Amplitude')
plt.savefig('yellowMercuryfig2.png')
plt.show()

plt.plot(yellowPos1,yellowAmp1,'-b')
plt.title('Yellow Doublet 1')
plt.xlabel('Position(µSteps)')
plt.ylabel('Amplitude')
plt.savefig('yellowMercuryfig1.png')
plt.show()