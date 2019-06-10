from playsound import playsound
from audioop import add, mul
from scipy.signal import fftconvolve
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
import wave
import sys

import soundfile as sf

def openWave(path, frames):
    with wave.open(path,'rb') as wave_file:
        if wave_file.getnchannels() == 2:
            raise Exception ('Arquivo stereo não suportado')
        
        params = wave_file.getparams()
        audio  = wave_file.readframes(frames)

    print("Número canais: ", params.nchannels)
    print("Número bytes: ", params.sampwidth)
    print("Taxa de amostragem: ", params.framerate)
    print("Número de frames: ", params.nframes)
    print("Compactação: ", params.compname)
    
    return params, audio

def output_wave(params, audio, path):
    with wave.open(path,'wb') as wave_file:
        wave_file.setparams(params)
        wave_file.writeframes(audio)

def gerarEcoWav(offset_ms = 1000, factor=1):
    ## abrir arquivo de audio e obter parametros de audio
    [params, audio] = openWave(path_origwav, frames)
    
    """ 'num' delays depois de 'offset_ms' milissegundos amplificado por 'fator'. """    
    if factor > 1:
        print('O audio resultante terá um volume alto')

    # calcular o número de bytes que correspondem ao offset em milissegundos
    offset = params.sampwidth * offset_ms * int(params.framerate/1000)

    # adicionar espaço extra no fim para o delay
    audio_bytes = audio + (b'\0' * offset)

    # cria uma copia do audio original para aplicar o delay
    delayed_bytes = audio_bytes

    # cria silencio
    inicio = b'\0' * offset

    # remove espaço do final
    fim = audio_bytes[:-offset]

    # multiplica por fator
    multiplied_end = mul(fim, params.sampwidth, factor**2)

    # adiciona os dois sinais para gerar o sinal com eco
    delayed_audio = add(delayed_bytes, inicio + multiplied_end, params.sampwidth)

    ## salvar audio com echo
    output_wave(params, delayed_audio, path_echowav)

def shift(xs, n):
    e = np.empty_like(xs)
    if n >= 0:
        e[:n] = 0.0
        e[n:] = xs[:-n]
    else:
        e[n:] = 0.0
        e[:n] = xs[-n:]
    return e

path_origwav = 'arquivos/sp04.wav'
path_echowav = 'arquivos/relatorio/sp04echo.wav'
path_echowav2 = 'arquivos/relatorio/sp04echo2.wav'
path_convwav = 'arquivos/relatorio/sp04conv.wav'

## um número grande arbitrário de frames
frames = 10000000
D = 500
a_list = [0.5,0.9,0.25]

for a in a_list:
    ## gerar audio com eco
    gerarEcoWav(D, a)

    [sp04, fs] = sf.read(path_origwav)
    [sp04echo, fsE] = sf.read(path_echowav)

    ## forma de onta de sp04.wav
    plt.figure(1)
    plt.subplot(211)
    plt.plot(sp04, linewidth=0.3, alpha=0.7, color='#004bc6')
    plt.title("Sinal 'sp04.wav' original")
    plt.xlabel("tempo (ms)")
    plt.ylabel("Amplitude (dB)")
    plt.grid(True)

    ## forma de onta de sp04echo.wav
    plt.subplot(212)
    plt.plot(sp04echo, linewidth=0.3, alpha=0.7, color='#004bc6')
    plt.title("Sinal 'sp04.wav' com eco (D = 500)")
    plt.xlabel("tempo (ms)")
    plt.ylabel("Amplitude (dB)")
    plt.grid(True)

    plt.show()

    ## Abrir o sinal original
    [signal_clean, fs] = sf.read('arquivos/sp04.wav')

    ## Resposta ao impulso
    [IR, fs] = sf.read('arquivos/relatorio/sp04echo.wav')

    ## Converte o formato do arquivo
    signal_clean=signal_clean.astype(np.float64)

    ## Normalização do sinal considerando o ponto de amplitude mais alta
    signal_clean=signal_clean/np.max(np.abs(signal_clean))
    IR=IR/np.abs(np.max(IR))

    p_max=np.argmax(np.abs(IR))

    ## efeito reverb pode ser obtido através da convolucao entre os sinais
    signal_rev=fftconvolve(signal_clean, IR, mode='full')

    ## Normalização do sinal considerando o ponto de amplitude mais alta
    signal_rev=signal_rev/np.max(np.abs(signal_rev))

    ## compensação de delay
    signal_rev=shift(signal_rev, -p_max)

    ## Cut reverberated signal (same length as clean sig)
    ## signal_rev=signal_rev[0:signal_clean.shape[0]]

    ## Salva arquivo final
    sf.write('arquivos/relatorio/sp04_reverb.wav', signal_rev, fs)

    ## forma de onta de sp04echo.wav
    plt.figure(2)
    plt.plot(signal_rev, linewidth=0.3, alpha=0.7, color='#004bc6')
    plt.title("convolucao - Sinal 'sp04.wav' com eco (D = 500)")
    plt.xlabel("tempo (ms)")
    plt.ylabel("Amplitude (dB)")
    plt.show()
