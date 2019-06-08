import imageio
import visvis as vv
from PIL import Image
from scipy import misc
from PIL import ImageFilter
from scipy.ndimage.filters import gaussian_filter


## carregar imagem
imgPath = 'arquivos/lena_rings.bmp'
imgFpath = 'arquivos/lena_rings_filtered_'

## abrir arquivo com a imagem    
img = Image.open(imgPath)

blurred_image = img.filter(ImageFilter.GaussianBlur(radius=1.2))
blurred_image2 = img.filter(ImageFilter.BoxBlur(radius=1.2))

## mostrar imagem original
img.show()

## mostrar imagem suavizada
blurred_image.show()
blurred_image2.show()

##lenaImg = imageio.imread(imgPath)
##
#### variacoes de modo
##lista_modo = ['reflect','constant','nearest','mirror','wrap']
##sigma = 2
##
##for modo in lista_modo:
##    ## variacoes de sigma
##    sigma = 1
##    maxSigma = 2
##    inc = 0.1
##
##    while sigma <= maxSigma:
##        ## aplicar filtro gaussiano com sigma
##        finalLenaImg = gaussian_filter(lenaImg, round(sigma,2), mode=modo)
##
##        ## salvar imagem resultante
##        imageio.imsave(imgFpath+modo+str(round(sigma,2)).replace('.','')+'.bmp',finalLenaImg)
##
##        sigma += inc
