from playsound import playsound
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

## Referencias:
## http://andrewslotnick.com/posts/audio-delay-with-python.html

from audioop import add, mul

def play_sound(file):
    playsound(file)

def delay(audio_bytes, params, offset_ms = 1000, factor=1, num=1):
    """ 'num' delays depois de 'offset_ms' milissegundos amplificado por 'fator'. """

    if factor > 1:
        print('O audio resultante terá um volume alto')

    # calcular o número de bytes que correspondem ao offset em milissegundos
    offset = params.sampwidth*offset_ms*int(params.framerate/1000)

    # adicionar espaço extra no fim para o delay
    audio_bytes = audio_bytes + b'\0'*offset*num

    # cria uma copia do audio original para aplicar o delay
    delayed_bytes = audio_bytes

    for i in range(num):
        # cria silencio
        inicio = b'\0'*offset

        # remove espaço do final
        fim = audio_bytes[:-offset]

        # multiplica por fator
        multiplied_end= mul(fim,params.sampwidth,factor**(i+1))
        
        delayed_bytes= add(delayed_bytes, inicio+multiplied_end, params.sampwidth)

    return delayed_bytes

def input_wave(filename,frames=10000000):
    #10000000 is an arbitrary large number of frames
    with wave.open(filename,'rb') as wave_file:
        params = wave_file.getparams()
        audio  = wave_file.readframes(frames)  
    return params, audio

#output to file so we can use ipython notebook's Audio widget
def output_wave(audio, params, filename):
    with wave.open(filename,'wb') as wave_file:
        wave_file.setparams(params)
        wave_file.writeframes(audio)

def test_stereo(wavFile):
    #If Stereo
    if wavFile.getnchannels() == 2:
        raise Exception ('Apenas arquivos mono...')

def print_data(file, params):
    print("\n\tFile: {}".format(file),
          "\n\tBytes per sample: {}".format(params.sampwidth),
          "\n\tSamples per second: {}".format(params.framerate))

def main():
    input_file = 'arquivos/sp04.wav'
    output_file = 'arquivos/sp04output.wav'

    wav = wave.open(input_file)
    test_stereo(wav)
    play_sound(input_file)
    
    input_params, input_bytes = input_wave(input_file)

    print_data(input_file, input_params)

    # delay de 1 segundo
    delay_file = delay(input_bytes, input_params)

    # salvar delay
    output_wave(delay_file, input_params, output_file)

    # Verificando saída
    output_params, output_bytes = input_wave(output_file)

    print_data(output_file, output_params)
    
    # reproduzir delay
    play_sound(output_file)  


main()
