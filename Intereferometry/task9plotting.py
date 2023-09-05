import numpy as np 
import matplotlib.pyplot as plt 
'''
1,5 = amplitude,position
'''
whiteAmp,whitePos = np.loadtxt('whiteLED_slow.txt',unpack = 'true', usecols = (1,5))
yellowAmp,yellowPos = np.loadtxt('yellowLED_fast.txt',unpack = 'true',usecols = (1,5))
greenAmp,greenPos = np.loadtxt('greenLED_fast.txt',unpack = 'true',usecols = (1,5))
blueAmp,bluePos = np.loadtxt('blueLED_GOOD.txt',unpack = 'true',usecols = (1,5))

plt.plot(whitePos,whiteAmp,'-b')
plt.title('White LED, No Filter')
plt.xlabel('Position(µSteps)')
plt.ylabel('Amplitude')
plt.savefig('whiteLEDfig')
plt.show()
plt.plot(yellowPos,yellowAmp,'-b')
plt.title('White LED, Yellow Filter')
plt.xlabel('Position(µSteps)')
plt.ylabel('Amplitude')
plt.savefig('yellowLEDfig')
plt.show()
plt.plot(greenPos,greenAmp,'-b')
plt.title('White LED, Green Filter')
plt.xlabel('Position(µSteps)')
plt.ylabel('Amplitude')
plt.savefig('greenLEDfig')
plt.show()
plt.plot(bluePos,blueAmp,'-b')
plt.title('Blue LED, No Filter')
plt.xlabel('Position(µSteps)')
plt.ylabel('Amplitude')
plt.savefig('blueLEDfig')
plt.show()