from numpy import angle, arange, hamming, spacing
from math import ceil, log10, pi, sin
from scipy.signal import freqz, lp2hp
from matplotlib import pyplot as plt

def ideal_hp(wc, M):
    ## Filtro Highpass Ideal:
    ## wc = frequência de corte
    ## M = comprimento do filtro ideal
    
    alpha = (M - 1)/2
    n = arange(0,M)
    m = [item - alpha + spacing(1) for item in n]

    ## inversão espectral: inverte todas as amostras
    ## e soma 1 a amostra central
    hd = [-sin(wc*item)/(pi*item) for item in m]
    hd[int(len(hd)/2)] += 1
    return hd

def freqz_m(b, a):
    ## Versao modificada da funcao freqz
    [w, H] = freqz(b, a, 1000, whole=True)
    H = H[:501]
    w = w[:501]
    mag = abs(H)
    maxMag = max(mag)
    db = [round(20*log10((item + spacing(1))/maxMag),5) for item in mag]
    pha = angle(H)

    return db, mag, pha, w

def highpassFIR(wp, ws):
    tr_width = abs(ws - wp)

    ## comprimento do filtro
    M = ceil(6.6 * pi / tr_width) + 1

    n = arange(0,M)

    wc = (ws + wp)/2

    ## resposta ao impulso
    hd = ideal_hp(wc, M)

    ## janela de hamming
    w_ham = hamming(M)

    ## fase linear
    h = hd*w_ham

    [db, mag, pha, w] = freqz_m(h, [1])

    delta_w = 2*pi/1000;

    ## ondulação na banda de passagem
    Rp = -(max(db[0:int(abs(wp)/delta_w)+1]))

    ## atenuação na banda de corte em dB
    As = -round(min(db[int(abs(ws)/delta_w):501]))

    return tr_width, M, n, wc, hd, w_ham, h, db, mag, pha, w, delta_w, Rp, As

## definição de parâmetros
ws = 0.6*pi
wp = 0.75*pi

tr_width, M, n, wc, hd, w_ham, h, db, mag, pha, w, delta_w, Rp, As = highpassFIR(wp, ws)

print('M = ', M)
print('alpha = ', (M - 1)/2)
print('Rp = ', Rp)
print('As = ', As)

## mostrar respostas
plt.figure(1)
plt.subplot(221)
plt.plot(hd,'bo')
plt.title('Resposta ao Impulso Ideal')
plt.xlabel('n')
plt.ylabel('hd[n]')
plt.grid(True)

plt.subplot(222)
plt.plot(w_ham)
plt.title('Janela de Hamming')
plt.xlabel('n')
plt.ylabel('w[n]')
plt.grid(True)

plt.subplot(223)
plt.plot(h,'bo')
plt.title('Resposta ao Impulso Atual')
plt.xlabel('n')
plt.ylabel('h[n]')
plt.grid(True)

plt.subplot(224)
plt.plot(w/pi, db)
plt.title('Magnitude em dB')
plt.xlabel('frequencia em pi unidades')
plt.ylabel('Decibeis')
plt.grid(True)

plt.show()
