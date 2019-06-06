from scipy.ndimage.filters import gaussian_filter
import imageio

class RingFilter:
    def __init__(self, nameImg='arquivos/lena_rings.bmp'):
        self.openImg(nameImg)
    
    def openImg(self, nameImg):
        self.originalImg = imageio.imread(nameImg)

    def getImgOriginal(self):
        return self.originalImg

    def getImgFiltrada(self):
        return self.filteredImg

    def salvarImg(self, path):
        imageio.imsave(path+'lena_rings_filtered_sigma'+str(self.sigma).replace('.','')+'.bmp',self.filteredImg)

    def aplicarFiltroRinging(self, sigma, path='arquivos/P2/Q1/'):
        self.sigma = round(sigma,2)
        self.filteredImg = gaussian_filter(self.originalImg, sigma)
        self.salvarImg(path)
