import math
import imageio
import cv2 as cv
from PIL import Image
from scipy.ndimage.filters import gaussian_filter

def detectarBordas(arquivo):
    lista_intensidade = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for intensidadeP in lista_intensidade:
        img = Image.open(arquivo)

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

        newimg.save('imagem'+str(intensidadeP)+'.bmp')

# https://medium.com/@lucashelal/detec%C3%A7%C3%A3o-e-contagem-da-%C3%A1rea-de-objetos-em-uma-imagem-bin%C3%A1ria-440759a7e034
# https://medium.com/@enzoftware/how-to-build-amazing-images-filters-with-python-median-filter-sobel-filter-%EF%B8%8F-%EF%B8%8F-22aeb8e2f540
path = 'arquivos/alumgrns.bmp'
path2 = 'arquivos/alumgrnsSuave.bmp'

## suavizar imagem
sigma = 0.5
filteredImg = gaussian_filter(imageio.imread(path), sigma)
imageio.imsave(path2, filteredImg)

## detectar bordas da imagem
detectarBordas(path2)

## converter imagem para Binario
img = cv.imread(path2, 0)
ret, imgT = cv.threshold(img, 127, 255, cv2.THRESH_BINARY)

plt.subplot(2,3,0)
plt.imshow(imgT,'gray')
plt.title('Imagem binaria')
plt.xticks([])
plt.yticks([])
plt.show()

