'''FFT_Sallam.py'''
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft 
#sr --->sampling rate, x---->list of time values, t---->list of time intervals, T---->sampling period, freq---->  frequency intervals 
def plot_fft(x,sr,t,xlabel1,xlabel2,ylabel1,ylabel2):
    X = fft(x)
    N = len(X)
    n = np.arange(N)
    T = N/sr
    freq = n/T 
    #LOW pass filter at 1 hz to eliminate the significance of the DC component 
    for i in range(len(freq)):
        if freq[i]>1 :
            break
        else: X[i]=0
    #HIGh pass filter at 20 hz to eliminate the significance of the high frequency components
    for i in range(len(freq)):
        if freq[i]>20 :
            X[i]=0
        

    plt.figure(figsize = (12, 6))
    plt.subplot(121)

    plt.plot(freq, np.abs(X/N)**2/max(np.abs(X/N))**2, 'hotpink')
    plt.xlabel(xlabel1)
    plt.ylabel(ylabel1)
    plt.xlim(0, 21)
    index = 0
    #printing the maximum amplitude along with the frequency coresponding to it  
    print(max(np.abs(X/N)))
    for i in range(len(X)):
        if abs(X[i]) == max(abs(X)):
            index = i
            break 
    print(freq[index])

    plt.subplot(122)
    plt.plot(t, x, 'g')
    plt.xlabel(xlabel2)
    plt.ylabel(ylabel2)
    plt.tight_layout()
    plt.show()