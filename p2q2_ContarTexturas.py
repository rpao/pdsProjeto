import math
import imageio
import cv2 as cv
import numpy as np
from PIL import Image
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
    cont = 0
    while fila:
        x,y  = fila.pop()
        for vizinho in vizinhos(img, x, y):
            xV, yV = vizinho
            corVizinho = img[xV][yV]
            if(corVizinho < corBorda and corVizinho != cor):
                img[xV][yV] = cor
                fila.append(vizinho)
        cont += 1
    return cont

## Aplicar uma busca em largura para pixels que possui o nível da cor escolhida
def contarAreas(img):
    pixelPintado = 5
    totalAreas = 0
    corBorda = 10
    rangeArea = 50
    for i in range(len(img)):
        for j in range(len(img[i])):
            cor = img[i][j]
            if cor < corBorda and cor != pixelPintado:
                cont = bfs(img,(i,j), pixelPintado, corBorda)
                if cont > rangeArea:
                    totalAreas += 1
            pixelPintado = 5
    return totalAreas

sigma = 1.5
intensidadeP = 10

path = 'arquivos/alumgrns.bmp'


## teste sem reducao de ruido
path_bordas = 'arquivos/relatorio/alumgrnsBordas.bmp'

print('Aplicando deteccao de bordas em imagem sem reducao de ruido')
detectarBordas(path, path_bordas, intensidadeP)

imgBordas = cv.imread(path_bordas, 0)

print('Iniciar contagem de texturas')
totalAreas = contarAreas(imgBordas);

print ('Total de Areas sem reducao de ruido: '+str(totalAreas))

## teste com reducao de ruido
lista_sigma = [0.5, 1.0, 1.5, 2]
for sigma in lista_sigma:
    path_suavizada = 'arquivos/relatorio/alumgrnsSuave'+str(sigma).replace('.','')+'.bmp'
    
    print('Aplicando reducao de ruido sigma=',sigma)
    suavizarBordas(path, path_suavizada, sigma)

    print('Aplicando deteccao de bordas em imagem com reducao de ruido')
    detectarBordas(path_suavizada, path_bordas, intensidadeP)

    imgBordas = cv.imread(path_bordas, 0)

    print('Iniciar contagem de texturas')
    totalAreas = contarAreas(imgBordas);

    print ('Total de Areas (sigma='+str(sigma)+'): '+str(totalAreas))
