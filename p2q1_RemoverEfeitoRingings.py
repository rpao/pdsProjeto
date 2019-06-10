from numpy import arange
from PIL.Image import open
from imageio import imread, imsave
from PIL.ImageFilter import GaussianBlur, BoxBlur
from scipy.ndimage.filters import gaussian_filter

#from scipy.ndimage.filters import gaussian_filter   
    
## carregar imagem
imgPath = 'arquivos/lena_rings.bmp'

list_radius = [0.3, 0.7, 1.1, 1.5, 1.9]
for r in list_radius:
    ## abrir arquivo com a imagem    
    img = open(imgPath)

    blurred_image = img.filter(GaussianBlur(radius=r))
    blurred_image2 = img.filter(BoxBlur(radius=r))

    ## mostrar imagem original
    ##img.show()

    ## mostrar imagem suavizada
    blurred_image.show()
    blurred_image2.show()

    ## salvar arquivos suavizados
    blurred_image.save('arquivos/relatorio/lena_rings_gaussian%2f.jpeg'%round(r,2))
    blurred_image2.save('arquivos/relatorio/lena_rings_BoxBlur%2f.jpeg'%round(r,2))

img = imread(imgPath)
for sigma in list_radius:
    imsave('arquivos/relatorio/lena_rings_gaussian2%2f.jpeg'%round(sigma,2), gaussian_filter(img, sigma))
