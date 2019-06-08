close all;
clear all;
clc;

%Questao 1

wp = 0.2*pi; ws = 0.3*pi;
tr_width = abs(ws - wp);
M = ceil(6.6*pi/tr_width) + 1;
n = [0:M-1];
wc = (ws + wp)/2;

%hd = ideal_lp(wc, M);
alpha = (M - 1)/2;
n = [0:(M-1)];
m = n - alpha + eps;
hd = sin(wc*m)./(pi*m);

w_ham = (hamming(M))';
h = hd.*w_ham;

% [db, mag, pha, w] = freqz_m(h, [1]);
[H, w] = freqz(h, [1], 1000, 'whole');
H = (H(1:501))'
w = (w(1:501))'
mag = abs(H);
db = 20*log10((mag + eps)/(max(mag)));
pha = angle(H);

delta_w = 2*pi/1000;
Rp = -(min(db(1:wp/delta_w+1)));
As = -round(max(db(ws/delta_w+1:501)));
subplot(1, 1, 1)
subplot (2, 2, 1); stem(n, hd); title('Resposta ao Impulso Ideal');
axis([0 M-1 -0.1 0.3]);xlabel('n');ylabel('hd[n]');
subplot (2, 2, 2); stem(n, w_ham); title('Janela de Hamming');
axis([0 M-1 0 1.1]);xlabel('n');ylabel('w[n]'); 

subplot (2, 2, 3); stem(n, h); title('Resposta ao Impulso Atual');
axis([0 M-1 -0.1 0.3]);xlabel('n');ylabel('h[n]');
subplot (2, 2, 4); plot(w/pi, db); title('Magnitude em dB');grid
axis([0 1 -100 10]);xlabel('frequencia em pi unidades');ylabel('Decibeis'); 