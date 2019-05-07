from playsound import playsound
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

## Referencias:
## http://andrewslotnick.com/posts/audio-delay-with-python.html

from audioop import add, mul

class Echo:
    def open(self, input_file):
        self.input_file = input_file
        self.wav = wave.open(input_file)

        if self.wav.getnchannels() == 2:
            raise Exception ('Arquivo stereo não suportado')

    def play_input(self):
        playsound(self.input_file)

    def play_output(self):
        playsound(self.output_file)

    def input_wave(self,frames=10000000):
        #10000000 is an arbitrary large number of frames
        with wave.open(self.input_file,'rb') as wave_file:
            self.params = wave_file.getparams()
            self.audio  = wave_file.readframes(frames)

    def getAudioInfo(self):
        return self.input_file,self.params.sampwidth,self.params.framerate,self.audio

    def printInputParams(self):
        print("\n\tFile: {}".format(self.input_file),
              "\n\tBytes per sample: {}".format(self.params.sampwidth),
              "\n\tSamples per second: {}".format(self.params.framerate))

    def printInputBytes(self):
        print("\n\tFile: {}".format(self.input_file),
              "\n\tAudio: {}".format(self.audio))

    def printOutputParams(self):
        print("\n\tFile: {}".format(self.output_file),
              "\n\tBytes per sample: {}".format(self.params.sampwidth),
              "\n\tSamples per second: {}".format(self.params.framerate))

    def printOutputBytes(self):
        print("\n\tFile: {}".format(self.output_file),
              "\n\tAudio: {}".format(self.delayed_audio))

    def delay(self, offset_ms = 1000, factor=1, num=1):
        """ 'num' delays depois de 'offset_ms' milissegundos amplificado por 'fator'. """

        if factor > 1:
            print('O audio resultante terá um volume alto')

        # calcular o número de bytes que correspondem ao offset em milissegundos
        offset = self.params.sampwidth*offset_ms*int(self.params.framerate/1000)

        # adicionar espaço extra no fim para o delay
        audio_bytes = self.audio + b'\0'*offset*num

        # cria uma copia do audio original para aplicar o delay
        delayed_bytes = audio_bytes

        for i in range(num):
            # cria silencio
            inicio = b'\0'*offset

            # remove espaço do final
            fim = audio_bytes[:-offset]

            # multiplica por fator
            multiplied_end= mul(fim,self.params.sampwidth,factor**(i+1))
            
            self.delayed_audio = add(delayed_bytes, inicio+multiplied_end, self.params.sampwidth)
            
        return self.delayed_audio

    def output_wave(self, output_file):
        self.output_file = output_file
        
        with wave.open(output_file,'wb') as wave_file:
            wave_file.setparams(self.params)
            wave_file.writeframes(self.delayed_audio)
        