import math
import imageio
import cv2 as cv
import numpy as np

from sys import argv
from PIL import Image
from matplotlib import pyplot as plt
from scipy.ndimage.filters import gaussian_filter

## suavizar imagem
def suavizarBordas(inputFile, outputFile, sigma):
    filteredImg = gaussian_filter(imageio.imread(inputFile), sigma)
    imageio.imsave(outputFile, filteredImg)

## Separar as areas detectando as bordas de separacao entre elas
def detectarBordas(inputFile, outputFile, intensidadeP):
    img = Image.open(inputFile)

    width, height = img.size

    newimg = Image.new("RGB", (width, height), "white")

    for x in range(1, width-1):  # ignora o pixel de bordar para simplificar (1 to width-1)
        for y in range(1, height-1): # ignora o pixel de bordar para simplificar (1 to height-1)
            Gx = 0
            Gy = 0

            # pixel mais alto a esquerda
            p = img.getpixel((x-1, y-1)) * intensidadeP

            # intensidade
            intensity = p

            # guarda o valor em Gx e Gy
            Gx += -intensity
            Gy += -intensity

            # coluna esquerda
            p = img.getpixel((x-1, y)) * intensidadeP
            Gx += -2 * p

            p = img.getpixel((x-1, y+1)) * intensidadeP
            Gx += -p
            Gy += p

            # pixels intermediarios
            p = img.getpixel((x, y-1)) * intensidadeP
            Gy += -2 * p

            p = img.getpixel((x, y+1)) * intensidadeP
            Gy += 2 * p

            # coluna direita
            p = img.getpixel((x+1, y-1)) * intensidadeP
            Gx += p
            Gy += -p

            p = img.getpixel((x+1, y)) * intensidadeP
            Gx += 2 * p

            p = img.getpixel((x+1, y+1)) * intensidadeP
            Gx += p
            Gy += p

            # calcular o tamanho do gradiente (Teorema Pythagorean)
            length = math.sqrt((Gx * Gx) + (Gy * Gy))

            # normalizar o tamanho do gradiente no intervalo de 0 ate 255
            length = length / 4328 * 255

            length = int(length)
            
            newimg.putpixel((x,y),length)

    newimg.save(outputFile)

# Busca dos vizinhos de um nó (4 pontos adjacentes a ele).
def vizinhos(img, x, y):
    vizinhos = []

    # vizinho a direita
    if (x+1 < len(img)):
        vizinhos.append((x+1, y))

    # vizinho a esquerda
    if (x-1 >= 0):
        vizinhos.append((x-1, y))

    # vizinho abaixo
    if (y+1 < len(img[x])):
        vizinhos.append((x, y+1))
        
    # vizinho acima
    if (y+1 >= 0):
        vizinhos.append((x, y-1))

    return vizinhos
    

#Marca como visitado a coordenada do pixel escolhido e verifica todos os vizinhos desse ponto
def bfs(img, ponto, cor, corBorda):
    i, j = ponto
    img[i][j] = cor
    fila = [ponto]
    while fila:
        x,y  = fila.pop()
        for vizinho in vizinhos(img, x, y):
            xV, yV = vizinho
            corVizinho = img[xV][yV]
            if(corVizinho < corBorda and corVizinho != cor):
                img[xV][yV] = cor
                fila.append(vizinho)

## Aplicar uma busca em largura para pixels que possui o nível da cor escolhida
def contarAreas(img):
    pixelPintado = 5
    totalAreas = 0
    corBorda = 10
    for i in range(len(img)):
        for j in range(len(img[i])):
            cor = img[i][j]
            if cor < corBorda and cor != pixelPintado:
                totalAreas += 1
                bfs(img,(i,j), pixelPintado, corBorda)
            pixelPintado += 5
    print ('Total de Areas: '+str(totalAreas))
    
# https://medium.com/@lucashelal/detec%C3%A7%C3%A3o-e-contagem-da-%C3%A1rea-de-objetos-em-uma-imagem-bin%C3%A1ria-440759a7e034
# https://medium.com/@enzoftware/how-to-build-amazing-images-filters-with-python-median-filter-sobel-filter-%EF%B8%8F-%EF%B8%8F-22aeb8e2f540

sigma = 0.5
lista_intensidadeP = [10,20,30,40,50,60,70,80,100]

intensidadeP = 20

#for intensidadeP in lista_intensidadeP:
path = 'arquivos/alumgrns.bmp'
path_suavizada = 'arquivos/P2/Q2/alumgrnsSuave.bmp'
path_bordas = 'arquivos/P2/Q2/alumgrns_intensidade'+str(intensidadeP)+'.bmp'

print('Aplicando suavizacao de ruidos')
suavizarBordas(path, path_suavizada, sigma)

print('Aplicando deteccao de bordas')
detectarBordas(path_suavizada, path_bordas, intensidadeP)

imgBordas = cv.imread(path_bordas, 0)

#print('Aplicando conversao de imagem para Binario')
#ret, imgT = cv.threshold(imgBordas, 127, 255, cv.THRESH_BINARY)

print('Iniciar contagem de texturas')
contarAreas(imgBordas);

    ## mostrar imagens
    #cv.imshow('original', imgBordas)
    #cv.imshow('pintada', imgT)

    #n,bins,patches = plt.hist(imgT.ravel(), 256, [1, 255])
    #plt.show()

    #input("Continuar?")

#### suavizar ruidos da imagem
##img = cv.imread(path_suavizada, 0)
##if (img == None):
##    suavizarBordas(path, path_suavizada, sigma)
##else:
##    opcao = input('A imagem com reducao de ruidos (' + path_suavizada + ') ja existe. Deseja utiliza-la, S|N?').upper()
##    if (opcao == 'N'):
##        print('Aplicando suavizacao de ruidos')
##        suavizarBordas(path, path_suavizada, sigma)
##        img = cv.imread(path_suavizada, 0)
##    else:
##        print('Carregando imagem "' + path_suavizada +'" pre-existente.')
##
#### detectar bordas da imagem
##imgBordas = cv.imread(path_bordas, 0)
##if (imgBordas == None):
##    detectarBordas(path_suavizada, path_bordas, intensidadeP)
##else:
##    opcao = input('A imagem com deteccao de bordas (' + path_bordas + ') ja existe. Deseja utiliza-la, S|N?').upper()
##    if (opcao == 'N'):
##        print('Aplicando deteccao de bordas')
##        detectarBordas(path_suavizada, path_bordas, intensidadeP)
##        imgBordas = cv.imread(path_bordas, 0)
##    else:
##        print('Carregando imagem "' + path_bordas +'" pre-existente.')

##plt.subplot(2,3,0)
##plt.imshow(imgT,'gray')
##plt.title('Imagem binaria')
##plt.xticks([])
##plt.yticks([])
##plt.show()

