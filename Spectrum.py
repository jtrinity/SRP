from matplotlib import pylab as plt
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
 
def getSpectrumAvg(signal_list, numStims):
    avgs = []
    for i in range(0, len(signal_list), numStims):
        avg = np.zeros(len(signal_list[0])/2)
        avg = avg.astype(np.complex128)
        
        for j in range(numStims):
            freq, Y = getSpectrum(signal_list[i+j])
            avg += np.array(Y)
        avg /= numStims
        #avg += i*np.ones(len(signal_list[0]))
        avgs.append((freq, avg))
        
    return avgs
    

