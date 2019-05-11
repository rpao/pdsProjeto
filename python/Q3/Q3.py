from imagemBmp import BMP

imagemName = "arquivos/lena_rings.bmp"

imgBmp = BMP()
img = imgBmp.openFile(imagemName)

print(img)
