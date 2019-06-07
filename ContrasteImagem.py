##import numpy as np
##import imageio
##
##def escalaCinza(img):
##    c = np.copy(img)
##
##    for x in range(len(img)):
##        for y in range(len(img[x])):
##            c[x][y] = int(0.31*img[x][y][2] + 0.52*img[x][y][1] + 0.11*img[x][y][0])
##
##    return c
##
##def converterCores(originalImg, indiceContraste):
##    img = np.copy(originalImg)    
##    img[:,:, 1] = 255/indiceContraste + (originalImg[:, :, 1] - originalImg[:, :, 0])  ## vermelho
##    img[:,:, 2] = 255/indiceContraste + (originalImg[:, :, 0] - originalImg[:, :, 1]) ## verde
##    img[:,:, 0] = 0  ## azul
##    return img
##
##nameImgOriginal='arquivos/dalton.bmp'
##originalImg = imageio.imread(nameImgOriginal)
##
##indiceContraste = int(input('Determine um indice de contraste: '))
##
##imgContraste = converterCores(originalImg, indiceContraste)
##nomeOutput = 'arquivos/P2/Q3/daltonContraste_' + str(indiceContraste) + '.bmp'
##imageio.imsave(nomeOutput,imgContraste)

from PIL import Image

## processando vermelho
def normalizarVermelho(intensidade):
    iI = intensidade
    minI = 86
    maxI = 230

    minO = 0
    maxO = 255
    
    iO = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
    return iO

## processando verde
def normalizarVerde(intensidade):
    iI = intensidade
    minI = 0
    maxI = 225

    minO = 0
    maxO = 255
    
    iO = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
    return iO

## processando azul
def normalizarAzul(intensidade):
    iI = intensidade
    minI = 200
    maxI = 210

    minO = 0
    maxO = 255
    
    iO = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
    return iO

imgPath='arquivos/dalton.bmp'
img = Image.open(imgPath)

## separar as bandas de vermelho, verde e azul
bandasRGB = img.split()

## aplicar stretching em cada banda
bandaR = bandasRGB[0].point(normalizarVermelho)
bandaG = bandasRGB[0].point(normalizarVerde)
bandaB = bandasRGB[0].point(normalizarAzul)

## gerar imagem final
imagemNormalizada = Image.merge("RGB", (bandaR, bandaG, bandaB))

## mostrar imagem original
img.show()

## mostrar imagem normalizada
imagemNormalizada.show()

## https://pythontic.com/image-processing/pillow/contrast%20stretching
