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

def gerar_senoide(duracao, frequencia, valorPico=0.5):
    """Gera um array numpy correspondente a uma senoide"""
    omega = pi * 2.0 * frequencia     
    tempo = arange(0, duracao, dtype=np.float)
    valorSinal = valorPico * sin(tempo * omega)    
    return valorSinal

## frequencia do ruído adicionado
frequencia_ruido = 466.16 #Hz

## Abrir o sinal original
[teste_som, sample_rate] = sf.read('arquivos/teste_de_som.wav')
print("Taxa de amostragem = ", sample_rate)

## Multiplica por 30
teste_som30 = 30*teste_som

## adicionar ruido
ruido = gerar_senoide(len(teste_som30), frequencia_ruido)
teste_som30 = teste_som30 + ruido

## forma de onta de sp04echo.wav
plt.figure(1)
plt.subplot(211)
plt.plot(teste_som, linewidth=0.3, alpha=0.7, color='#c7135c')
plt.title("Sinal 'teste_de_som.wav' original")
plt.xlabel("tempo (ms)")
plt.ylabel("Amplitude (dB)")
plt.grid(True)

plt.subplot(212)
plt.plot(teste_som30, linewidth=0.3, alpha=0.7)
plt.title("Sinal 'teste_de_som.wav' amplificado de 30 com adição de ruído")
plt.xlabel("tempo (ms)")
plt.ylabel("Amplitude (dB)")
plt.grid(True)

sf.write('arquivos/relatorio/teste_som30_ruidosenoidal_466.16Hz.wav', teste_som30, sample_rate)

## FILTRO FIR
nsamples = len(teste_som30)
t = arange(nsamples) / sample_rate

# The Nyquist rate of the signal.
nyq_rate = sample_rate / 2.0

# The desired width of the transition from pass to stop,
# relative to the Nyquist rate.  We'll design the filter
# with a 5 Hz transition width.
width = 5.0/nyq_rate

# The desired attenuation in the stop band, in dB.
ripple_db = 60.0

# Compute the order and Kaiser parameter for the FIR filter.
N, beta = kaiserord(ripple_db, width)

# The cutoff frequency of the filter.
cutoff_list = [3000/nyq_rate,1000/nyq_rate, 500/nyq_rate]

taps_list = []
cont = 2
for cutoff_hz in cutoff_list:
    # Use firwin with a Kaiser window to create a lowpass FIR filter.
    taps_list.append([firwin(N, cutoff_hz, window=('kaiser', beta)), 'kaiser', cutoff_hz])
    taps_list.append([firwin(N, cutoff_hz, window='hamming'),'hamming', cutoff_hz])
    taps_list.append([firwin(N, cutoff_hz, window='hamming'),'gaussian', cutoff_hz])

for taps, name, cutoff in taps_list:

    # Use lfilter to filter x with the FIR filter.
    filtered_audio = lfilter(taps, 1.0, teste_som30)

    # The phase delay of the filtered signal.
    delay = 0.5 * (N-1) / sample_rate

    figure(cont)
    # Plot filtered signal
    plot(t-delay, filtered_audio, 'r-', linewidth=0.3, alpha=0.7)
    plot(t[N-1:]-delay, filtered_audio[N-1:], 'g', linewidth=0.3,  alpha=0.7)
    plot(t, teste_som, linewidth=0.3,  alpha=0.7)
    title('Saída do filtro FID - janela: ' + name + ', cutoff = ' + str(round(cutoff,3)))
    xlabel('tempo(s)')
    ylabel('Amplitude')
    grid(True)

    cont+= 1

    ## Salva arquivo final
    sf.write('arquivos/relatorio/teste_de_som_FIR_'+name+'_'+str(cutoff)+'.wav', filtered_audio, sample_rate)

show()
