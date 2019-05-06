import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

def genEcho(wav, scale):
    echo = [wav[i]*scale for i in range(len(wav))]
    return echo

def addEcho(wav, delay, scale):
    echo = genEcho(wave, scale)
    

def plotWav(signal, echoSignal):
    plt.subplot(2,1,1)
    plt.plot(signal)

    plt.subplot(2,1,2)
    plt.plot(echoSignal)
    
    plt.figure(1)
    plt.title('Signal Wave...')
    plt.show()

scale = 0.5
delay = 100
spf = wave.open('arquivos/sp04.wav')

#If Stereo
if spf.getnchannels() == 2:
    print ('Just mono files')
    sys.exit(0)

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')

echo = addEcho(signal, scale)

plotWav(signal,echo)

#### spf = wave.open('wavfile.wav','r')
##
###Extract Raw Audio from Wav File
##signal = spf.readframes(-1)
##signal = np.fromstring(signal, 'Int16')
##
##
###If Stereo
##if spf.getnchannels() == 2:
##    print ('Just mono files')
##    sys.exit(0)
##
##plt.figure(1)
##plt.title('Signal Wave...')
##plt.plot(signal)
##plt.show()
