
import matplotlib.pyplot as plt
import numpy as np
import math

Fs     = 44100.0  # Sampling rate (Hz)
f      = 440.0    # Frequency (Hz)

Ts     = 1.0/Fs # Sampling interval
sampleLength = 0.01 # s
t      = np.arange(0,sampleLength,Ts)

# sine wave
y = np.sin(2 * np.pi * f * t)

#plt.plot(x, y)
#plt.xlabel('time sample(n)')
#plt.ylabel('amplitude')
#plt.show()

#freq = np.fft.fftfreq(sample, d=1.0/Fs)
#fft_data = np.fft.fft(y)
#plt.plot(freq, fft_data)
#plt.show()

n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides of frequency range
frq = frq[range(n/2)]

Y = np.fft.fft(y)/n
Y = Y[range(n/2)]

maxFreqIdx = np.argmax(abs(Y))
print("Max freq = %f Hz" %frq[maxFreqIdx])

fig, ax = plt.subplots(2, 1)
ax[0].plot(t,y)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[1].plot(frq,abs(Y),'r') # plotting the spectrum
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')
plt.show()
