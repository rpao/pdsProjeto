import math
import numpy as np
from scipy.signal import freqz
from matplotlib import pyplot as plt

def ideal_lp(wc, M):
    ## Ideal low pass filter: wc = cutoff frequency e M = length of the ideal filter
    alpha = (M - 1)/2
    n = np.arange(0,M)
    m = [item - alpha + np.spacing(1) for item in n]
    hd = [math.sin(wc*item)/(math.pi*item) for item in m]
    return hd

def freqz_m(b, a):
    ## Versao modificada da funcao freqz
    [w, H] = freqz(b, a, 1000, whole=True)
    H = H[:501]
    w = w[:501]
    mag = abs(H)
    maxMag = max(mag)
    db = [20*math.log10((item + np.spacing(1))/maxMag) for item in mag]
    pha = np.angle(H)

    return db, mag, pha, w

## definição de parâmetros
wp = 0.2*math.pi
ws = 0.3*math.pi

tr_width = abs(ws - wp)

M = math.ceil(6.6 * math.pi / tr_width) + 1

n = np.arange(0,M)

wc = (ws + wp)/2

hd = ideal_lp(wc, M)

w_ham = np.hamming(M)

h = hd*w_ham

[db, mag, pha, w] = freqz_m(h, [1])

delta_w = 2*math.pi/1000;
indice = int(ws/delta_w)
Rp = -(min(db[0:indice]))
As = -(round(max(db[indice:501])))

## mostrar respostas
plt.figure(1)
plt.subplot(211)
plt.plot(n,hd)
plt.title('Resposta ao Impulso Ideal')
plt.xlabel('n')
plt.ylabel('hd[n]')

plt.subplot(212)
plt.plot(n,w_ham)
plt.title('Janela de Hamming')
plt.xlabel('n')
plt.ylabel('w[n]')

plt.figure(2)
plt.subplot(211)
plt.plot(n,h)
plt.title('Resposta ao Impulso Atual')
plt.xlabel('n')
plt.ylabel('h[n]')

plt.subplot(212)
plt.plot(w/math.pi, db)
plt.title('Magnitude em dB')
plt.xlabel('frequencia em pi unidades')
plt.ylabel('Decibeis')

plt.show()
