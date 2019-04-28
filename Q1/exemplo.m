%% ESPECIFICACOES DO FILTRO
ws = 0.6*pi;
wp = 0.75*pi; 
As = 50;

%% Janela de Kaiser
% calculando deltaW
tr_width = abs(ws - wp);

% calculando M, beta e Wc
% M = ceil((As - 7.95)/(14.36*tr_width/(2*pi))+1) + 1;
M = ceil((As - 8)/(2.285*tr_width) + 1) + 1;

n = 0:M-1;
beta = 0.1102*(As - 8.7);
wc = (ws + wp)/2;

% resposta ao impulso ideal de um filtro passa-baixa
hd = ideal_lp(wc, M);

% Janela de kaiser
w_kai = (kaiser(M, beta))';
h = hd.*w_kai;
[db, mag, pha, w] = freqz_m(h, [1]);
delta_w = 2*pi/1000;
As = -round(max(db(ws/delta_w+1:501)));

% Plot
subplot(1, 1, 1)
subplot (2, 2, 1); stem(n, hd); title('Resposta ao Impulso Ideal');
axis([0 M-1 -0.1 0.3]);xlabel('n');ylabel('hd[n]');
subplot (2, 2, 2); stem(n, w_kai); title('Janela de Kaiser');
axis([0 M-1 0 1.1]);xlabel('n');ylabel('w[n]');
subplot (2, 2, 3); stem(n, h); title('Resposta ao Impulso Atual');
axis([0 M-1 -0.1 0.3]);xlabel('n');ylabel('h[n]');
subplot (2, 2, 4); plot(w/pi, db); title('Magnitude em dB');grid
axis([0 1 -100 10]);xlabel('frequencia em pi unidades');ylabel('Decibeis');

% hd = ideal_lp (wc, M);
% w_ham = (hamming(M))';
% h = hd.*w_ham;
% [db, mag, pha, w] = freqz_m(h, [1]);
% delta_w = 2*pi/1000;
% Rp = -(min(db(1:wp/delta_w+1)))
% As = -round(max(db(ws/delta_w+1:501)))

% subplot(1, 1, 1)
% subplot (2, 2, 1); stem(n, hd); title('Resposta ao Impulso Ideal');
% axis([0 M-1 -0.1 0.3]);
% xlabel('n');ylabel('hd[n]');
% subplot (2, 2, 2); stem(n, w_ham); 
% title('Janela de Hamming');
% axis([0 M-1 0 1.1]);xlabel('n');ylabel('w[n]');
% 
% subplot (2, 2, 3); stem(n, h); title('Resposta ao Impulso Atual');
% axis([0 M-1 -0.1 0.3]);xlabel('n');ylabel('h[n]');
% subplot (2, 2, 4); plot(w/pi, db); title('Magnitude em dB');grid
% axis([0 1 -100 10]);xlabel('frequencia em pi unidades');ylabel('Decibeis');
% 
% M = 67
% alpha = 33
% Rp = 0,0394
% As = 52

% fdatool => filterDesigner