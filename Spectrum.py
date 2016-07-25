
import numpy as np


def getSpectrum(signal):
 """
 Plots a Single-Sided Amplitude Spectrum of y(t)
 """
 length = len(signal)
 k = np.arange(length)
 T = length/1000.0
 frequency = k/T # two sides frequency range
 frequency = frequency[range(length/2)] # one side frequency range

 Y = np.fft.fft(signal)/length # fft computing and normalization
 Y = Y[range(length/2)]
 
 return frequency, Y
 
