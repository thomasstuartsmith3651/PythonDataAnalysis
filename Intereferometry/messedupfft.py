import sys
import read_data_results3 as rd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy import signal
import scipy.fftpack as spf
import scipy.signal as sps
import scipy.interpolate as spi
import scipy.stats as spst

#file='%s'%(sys.argv[1]) #this is the data
results = rd.read_data3('whiteLED_slow.txt')

y2 = np.array(results[0])
y1 = np.array(results[1])
x=np.array(results[5])

#step 2.1 butterworth filter to correct for misaligment (offset)
filter_order = 2
freq = 1 #cutoff frequency
sampling = 50 # sampling frequency
sos = signal.butter(filter_order, freq, 'hp', fs=sampling, output='sos')
filtered = signal.sosfilt(sos, y1)
y1 = filtered
filtered = signal.sosfilt(sos, y2)
y2 = filtered


x = x[100:]
y1 = y1[100:]

nsamp = len(x) #number of readings that you will take (set in the software)
#dist_per_step = 1.56e-11 * 2 #distance moved (new apparatus prob. 1nm step*2 for path length)
#dist_per_step = 531.8e-9 / (2 * 7101)
steps_per_sample = 15000/50
dist_per_step = 546e-9 / 14750
steps_per_sample = np.average(np.diff(results[5]))
dsamp = dist_per_step * steps_per_sample

# take a fourier transform
yf=spf.ifft(y1)
xf=spf.fftfreq(nsamp) # setting the correct x-axis for the fourier transform. Osciallations/step

#now some shifts to make plotting easier (google if ineterested)
xf=spf.fftshift(xf)
yf=spf.fftshift(yf)

plt.figure(1)
plt.plot(xf,np.abs(yf))
plt.xlabel("Oscillations per sample")
plt.ylabel("Amplitude")

xx=xf[int(len(xf)/2+1):len(xf)]
repx=dsamp/xx


plt.figure(2)
plt.plot(repx,abs(yf[int(len(xf)/2+1):len(xf)]))
plt.xlabel("Wavelength (m)")
plt.ylabel("Amplitude")
plt.title(' FFT')
plt.xlim(1e-7,20e-7)

#plt.vlines(531.8e-9, min(abs(yf[int(len(xf)/2+1):len(xf)])), max(abs(yf[int(len(xf)/2+1):len(xf)])), colors='gray', linestyles='dashed')
plt.savefig('yellowfft.png')
plt.show()


plt.figure(3)
plt.plot(range(len(y1)),y1)
plt.title('White LED, No Filter')
plt.xlabel('Position(µSteps)')
plt.ylabel('Amplitude')
plt.savefig('whiteLEDfig')
plt.show()



plt.show()