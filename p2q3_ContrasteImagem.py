from PIL import Image

"""
Aplica a operação de stretch para alterar o contraste da imagem e separar as cores.

formula de normalizacao:
 iO = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
iO é a intensidade do pixel resultante da normalização,
iI é a intensidade original do pixel,
minI é o menor valor da intensidade do pixel original,
minO é o menor valor da intensidade do pixel resultante = 0,
maxI é o maior valor da intensidade do pixel original
maxO é o maior valor da intensidade do pixel resultante da normalização = 255.
"""

## normalizando a banda vermelho (R)
def normalizarVermelho(intensidade):
    iI = intensidade
    iO = iI
    minI = 86
    maxI = 230

    minO = 0
    maxO = 255
    
    iO = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
    return iO

## normalizando a banda verde (G)
def normalizarVerde(intensidade, teste = 1):
    iI = intensidade
    
    minI = 100
    maxI = 230

    minO = 0
    maxO = 255
        
    iO = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
    return iO

## normalizando a banda azul (B)
def normalizarAzul(intensidade):
    iI = intensidade
    minI = 200
    maxI = 210

    minO = 0
    maxO = 255
    
    iO = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
    return iO

imgPath='arquivos/dalton.bmp'

## abrir arquivo com a imagem    
img = Image.open(imgPath)

## separar as bandas de vermelho, verde e azul
bandasRGB_teste1 = img.split()
bandasRGB_teste2 = img.split()

## aplicar stretching em cada banda - teste 1
## como minI = minO e maxI = maxO, log iO = iI, logo não precisa aplicar a normalizacao
bandaR1 = bandasRGB_teste1[0].point(normalizarVermelho)
bandaG1 = bandasRGB_teste1[0]
bandaB1 = bandasRGB_teste1[0].point(normalizarAzul)

## aplicar stretching em cada banda - teste 2
bandaR2 = bandasRGB_teste2[0].point(normalizarVermelho)
bandaG2 = bandasRGB_teste2[0].point(normalizarVerde)
bandaB2 = bandasRGB_teste2[0].point(normalizarAzul)

## gerar imagem final - teste 1
imagemNormalizada1 = Image.merge("RGB", (bandaR1, bandaG1, bandaB1))

## gerar imagem final - teste 2
imagemNormalizada2 = Image.merge("RGB", (bandaR2, bandaG2, bandaB2))

## mostrar imagem original
img.show()

## mostrar imagem normalizada - teste 1
imagemNormalizada1.show()

## mostrar imagem normalizada - teste 2
imagemNormalizada2.show()

## https://pythontic.com/image-processing/pillow/contrast%20stretching
