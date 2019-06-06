import numpy as np
import imageio

class ContrasteImagem:
    def __init__(self, nameImg='arquivos/dalton.bmp'):
        self.openImg(nameImg)
    
    def openImg(self, nameImg):
        self.originalImg = imageio.imread(nameImg)

    def getImgOriginal(self):
        return self.originalImg

    def salvarImg(self, path, complementoNome=''):
        imageio.imsave(path+'dalton_comContraste_'+self.RGB+'_'+complementoNome+'.bmp',self.imgContraste)

    def aplicarContraste(self, RGB = 'R', indiceContraste = 2, path = 'arquivos/P2/Q3/'):
        self.RGB = RGB.upper()
        if self.RGB == 'R':
            self.aplicarContrasteVermelho(indiceContraste, path)
        elif self.RGB == 'G':
            self.aplicarContrasteVerde(indiceContraste, path)
        elif self.RGB == 'B':
            self.aplicarContrasteAzul(indiceContraste, path)
        else:
            raise Exception('Opcao RGB invalida')            

    def aplicarContrasteAzul(self, indiceContraste, path):
        img = np.copy(self.originalImg)
        img[:,:, 0] = 255/indiceContraste + (self.originalImg[:, :, 0] - self.originalImg[:, :, 1])
        img[:,:, 1] = 255/indiceContraste + (self.originalImg[:, :, 1] - self.originalImg[:, :, 0])
        img[:,:, 2] = 0

        self.imgContraste = img
        self.salvarImg(path, str(indiceContraste).replace('.',''))

    def aplicarContrasteVerde(self, indiceContraste, path):
        img = np.copy(self.originalImg)
        img[:, 0, :] = 255/indiceContraste + (self.originalImg[:, 0, :] - self.originalImg[:, 1, :])
        img[:, 1, :] = 255/indiceContraste + (self.originalImg[:, 1, :] - self.originalImg[:, 0, :])
        img[:, 2, :] = 0

        self.imgContraste = img
        self.salvarImg(path, str(indiceContraste).replace('.',''))

    def aplicarContrasteVermelho(self, indiceContraste, path):
        img = np.copy(self.originalImg)
        img[0,:, :] = 255/indiceContraste + (self.originalImg[0, :, :] - self.originalImg[1, :, :])
        img[1,:, :] = 255/indiceContraste + (self.originalImg[1, :, :] - self.originalImg[0, :, :])
        img[2,:, :] = 0

        self.imgContraste = img
        self.salvarImg(path, str(indiceContraste).replace('.',''))
        
    def getImgContraste(self):
        return self.imgContraste
