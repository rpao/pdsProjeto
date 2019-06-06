from PIL import Image
import math

# https://medium.com/@enzoftware/how-to-build-amazing-images-filters-with-python-median-filter-sobel-filter-%EF%B8%8F-%EF%B8%8F-22aeb8e2f540
path = "arquivos/alumgrns.bmp" # Your image path
lista_intensidade = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for intensidadeP in lista_intensidade:
    img = Image.open(path)

    width, height = img.size

    newimg = Image.new("RGB", (width, height), "white")

    for x in range(1, width-1):  # ignore the edge pixels for simplicity (1 to width-1)
        for y in range(1, height-1): # ignore edge pixels for simplicity (1 to height-1)

            # initialise Gx to 0 and Gy to 0 for every pixel
            Gx = 0
            Gy = 0

            # top left pixel
            p = img.getpixel((x-1, y-1)) * intensidadeP

            # intensity ranges from 0 to 765 (255 * 3)
            intensity = p

            # accumulate the value into Gx, and Gy
            Gx += -intensity
            Gy += -intensity

            # remaining left column
            p = img.getpixel((x-1, y)) * intensidadeP
            Gx += -2 * p

            p = img.getpixel((x-1, y+1)) * intensidadeP
            Gx += -p
            Gy += p

            # middle pixels
            p = img.getpixel((x, y-1)) * intensidadeP
            Gy += -2 * p

            p = img.getpixel((x, y+1)) * intensidadeP
            Gy += 2 * p

            # right column
            p = img.getpixel((x+1, y-1)) * intensidadeP
            Gx += p
            Gy += -p

            p = img.getpixel((x+1, y)) * intensidadeP
            Gx += 2 * p

            p = img.getpixel((x+1, y+1)) * intensidadeP
            Gx += p
            Gy += p

            # calculate the length of the gradient (Pythagorean theorem)
            length = math.sqrt((Gx * Gx) + (Gy * Gy))

            # normalise the length of gradient to the range 0 to 255
            length = length / 4328 * 255

            length = int(length)

            # draw the length in the edge image
            #newpixel = img.putpixel((length,length,length))
            newimg.putpixel((x,y),(length,length,length))

    newimg.save('imagem'+str(intensidadeP)+'.bmp')

##import numpy as np
##import scipy as sc
##import imageio
##
##from PIL import Image
##from scipy.ndimage.filters import gaussian_filter
##
#### referencia:
#### https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123
##
##class ContarTexturas:
##    def __init__(self, sigma=1, nome='alumgrns.bmp', path='arquivos/'):
##        self.nomeImg = nome
##        self.pathImg = path
##        self.reduzirRuido(sigma)
####        self.img = Image.open(path+nome)
##        
####    def getImagem(self):
####        return self.img
##
##    ## Aplicar o filtro gaussiano para reduzir o ruido da imagem
##    def reduzirRuido(self, sigma):
##        img = imageio.imread(self.pathImg + self.nomeImg)
##
##        self.sigma = round(sigma,2)
##        imgGaussiana = gaussian_filter(img, sigma)
##        imageio.imsave(self.pathImg + 'P2/Q2/reduzirRuido_' + self.nomeImg, imgGaussiana)
##
##    
##    Redução de ruido
##    def reduzirRuido(self, tamanho, sigma=1):
##        ## Tecnica de Convolução - Aplicando Gaussian Blur para reduzir o ruído
##        ## kernel: quanto menor, menor a reducao
##        tamanho = int(tamanho)//2 ##
##        x, y = np.mgrid[-tamanho:tamanho+1, -tamanho:tamanho+1]
##        normal = 1 / (2. * np.pi * sigma**2)
##        g = np.exp(-(x**2 + y**2) / (2.0*sigma**2))) * normal
##
##        return g
##
##    Realcar bordas
##    def filtroRealce(self):
##        ## Calculo do gradiente:
##        ## Detecta a intensidade das bordas e direções calculando o gradiente da imagem
##        ## usando operadores de deteccao de bordas.
##        ## Bordas correspondem a mudancas na intensidade dos pixels, para detecta-las
##        ## sera aplicado um filtro que realca a intensidade dessas mudancas (vertical e
##        ## horizontal)
##
##        Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
##        Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)
##        
##        Ix = sc.filters.convolve(self.img, Kx)
##        Iy = sc.filters.convolve(self.img, Ky)
##        
##        G = np.hypot(Ix, Iy)
##        G = G / G.max() * 255
##        theta = np.arctan2(Iy, Ix)
##        
##        return (G, theta)
        
