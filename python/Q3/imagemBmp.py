import matplotlib.pyplot as plt
import numpy as np
import sys

#Referências
#https://stackoverflow.com/questions/20276458/working-with-bmp-files-in-python-3
class BMP:
    #def __init__(self):

    def openFile(self, name):
        self.nameFile = name
        with open(self.nameFile, 'rb') as f:
            self.data = bytearray(f.read())

        return self.data

    
