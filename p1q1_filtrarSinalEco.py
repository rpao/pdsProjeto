from playsound import playsound
from audioop import add, mul
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

## Referencias:
## http://andrewslotnick.com/posts/audio-delay-with-python.html

def openwav(file):
    wav = wave.open(file)
    if wav.getnchannels() == 2:
        raise Exception ('Arquivo stereo não suportado')
    return wav

def input_wave(path, frames):
    with wave.open(path,'rb') as wave_file:
        params = wave_file.getparams()
        audio  = wave_file.readframes(frames)
    return params, audio

def output_wave(params, audio, path):
    with wave.open(path,'wb') as wave_file:
        wave_file.setparams(params)
        wave_file.writeframes(audio)

def delay(params, audio, offset_ms = 1000, factor=1, num=1):
    """ 'num' delays depois de 'offset_ms' milissegundos amplificado por 'fator'. """    
    if factor > 1:
        print('O audio resultante terá um volume alto')

    # calcular o número de bytes que correspondem ao offset em milissegundos
    offset = params.sampwidth * offset_ms * int(params.framerate/1000)

    # adicionar espaço extra no fim para o delay
    audio_bytes = audio + (b'\0' * offset * num)

    # cria uma copia do audio original para aplicar o delay
    delayed_bytes = audio_bytes

    for i in range(num):
        # cria silencio
        inicio = b'\0' * offset

        # remove espaço do final
        fim = audio_bytes[:-offset]

        # multiplica por fator
        multiplied_end = mul(fim, params.sampwidth, factor**(i+1))
        
        delayed_audio = add(delayed_bytes, inicio + multiplied_end, params.sampwidth)
        
    return delayed_audio

path_origwav = 'arquivos\sp04.wav'
path_echowav = 'arquivos\sp04echo.wav'

##um número grande arbitrário de frames
frames = 10000000

offset = 500
factor = 0.5
num=1

## abrir arquivo de audio
inWav = openwav(path_origwav)

## obter parametros de audio
[params, audio] = input_wave(path_origwav, frames)

## inserir eco
delayAudio = delay(params, audio, offset, factor, num)

## salvar audio com echo
output_wave(params, delayAudio, path_echowav)

## abrir arquivo de audio
echo = openwav(path_echowav)

playsound(path_origwav)
playsound(path_echowav)


