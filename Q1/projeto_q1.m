% definicoes do problema
wp = 0.4*pi;
ws = 0.6*pi;
delta = 0.001;

% calculando wc
wc = (ws + wp)/2;

% calculando delta W
dW = ws - wp;

% calculando A
A = -20*log10(delta);

% calculando beta
if (A > 50)
    beta = 0.1102*(A - 8.7);
elseif (A >= 21) && (A <= 50)
    beta = 0.5842*(A - 21) + 0.07886*(A - 21);
else
    beta = 0;
end

% calculando M
M = (A - 8)/(2.285*dW);

% janela Kaiser:
w = kaiser(M, beta);

% a resposta ao impulso é:
n = 0:size(w);

h = sin(wc*(n-M/2))/(pi*(n-M/2))*w