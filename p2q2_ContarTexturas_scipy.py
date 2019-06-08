import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('arquivos/alumgrns.bmp',0)

## detecta bordas utilizando derivadas laplaciana
imgLaplacian = cv.Laplacian(img,cv.CV_64F)

## img binary
ret,thresh_img1 = cv.threshold(imgLaplacian,10,80,cv.THRESH_BINARY)

plt.subplot(3,1,1),plt.imshow(img,cmap = 'gray')
plt.title('img'), plt.xticks([]), plt.yticks([])
plt.subplot(3,1,2),plt.imshow(imgLaplacian,cmap = 'gray')
plt.title('0'), plt.xticks([]), plt.yticks([])
plt.subplot(3,1,3),plt.imshow(thresh_img1,cmap = 'gray')
plt.title('50'), plt.xticks([]), plt.yticks([])
##plt.subplot(3,2,4),plt.imshow(thresh_img3,cmap = 'gray')
##plt.title('100'), plt.xticks([]), plt.yticks([])
##plt.subplot(3,2,5),plt.imshow(thresh_img4,cmap = 'gray')
##plt.title('150'), plt.xticks([]), plt.yticks([])
##plt.subplot(3,2,6),plt.imshow(thresh_img5,cmap = 'gray')
##plt.title('200'), plt.xticks([]), plt.yticks([])

plt.show()

## https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_gradients/py_gradients.html



