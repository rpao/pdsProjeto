##import os
##import sys
##import numpy as np
##from numpy import arange
##
##from scipy.signal import firwin, lfilter
##
##from numpy import cos, sin, pi

import numpy as np
import soundfile as sf
from numpy import pi, absolute, arange, sin
from scipy.signal import kaiserord, lfilter, firwin, firwin2, freqz, get_window
from pylab import figure, clf, plot, xlabel, ylabel, xlim, ylim, title, grid, axes, show
import matplotlib.pyplot as plt

## Abrir o sinal original
[car1, sample_rate] = sf.read('arquivos/car1.wav')
print("Taxa de amostragem = ", sample_rate)

## forma de onta de sp04echo.wav
plt.figure(1)
plt.subplot(211)
plt.plot(car1, linewidth=0.3, alpha=0.7, color='#c7135c')
plt.title("Sinal 'car1.wav' original")
plt.xlabel("tempo (ms)")
plt.ylabel("Amplitude (dB)")
plt.grid(True)

## FILTRO FIR
nsamples = len(car1)
t = arange(nsamples) / sample_rate

# The Nyquist rate of the signal.
nyq_rate = sample_rate / 2.0
width = 5.0/nyq_rate

# The desired attenuation in the stop band, in dB.
ripple_db = 60.0

# Compute the order and Kaiser parameter for the FIR filter.
N, beta = kaiserord(ripple_db, width)

# The cutoff frequency of the filter.
cutoff_list = [3000/nyq_rate,1000/nyq_rate, 500/nyq_rate]
cont = 2
for cutoff_hz in cutoff_list:
    # Use firwin with a Kaiser window to create a lowpass FIR filter.
    taps_list.append([firwin(N, cutoff_hz, window=('kaiser', beta)), 'kaiser', cutoff_hz])
    taps_list.append([firwin(N, cutoff_hz, window='hamming'),'hamming', cutoff_hz])

for taps, name, cutoff in taps_list:

    # Use lfilter to filter x with the FIR filter.
    filtered_audio = lfilter(taps, 1.0, car1)

    # The phase delay of the filtered signal.
    delay = 0.5 * (N-1) / sample_rate

    figure(cont)
    # Plot filtered signal
    plot(t-delay, filtered_audio, 'r-', linewidth=0.3, alpha=0.7)
    plot(t[N-1:]-delay, filtered_audio[N-1:], 'g', linewidth=0.3,  alpha=0.7)
    plot(t, car1, linewidth=0.3,  alpha=0.7)
    title('Saída do filtro FID - janela: ' + name + ', cutoff = ' + str(round(cutoff,3)))
    xlabel('tempo(s)')
    ylabel('Amplitude')
    grid(True)

    cont+= 1

    ## Salva arquivo final
    sf.write('arquivos/relatorio/car1_FIR'+name+'_'+str(cutoff)+'.wav', filtered_audio, sample_rate)

show()
