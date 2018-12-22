
import matplotlib.pyplot as plt
import numpy
import math

#sample=16
#a=[0]*sample
#for i in range(sample):
#  a[i] = math.sin(2*math.pi*i)

#f = numpy.fft.fft(a)

#for idx,s in enumerate(f):
#  if s != 0:
#    print("f[%d] = %s" %(idx,s))

Fs = 8000
f = 5
sample = 8000
x = numpy.arange(sample)
y = numpy.sin(2 * numpy.pi * f * x / Fs)
plt.plot(x, y)
plt.xlabel('time sample(n)')
plt.ylabel('amplitude')
plt.show()

freq = numpy.arange(16000)
f = numpy.fft.fft(y)
plt.plot(freq, f)
plt.show()
