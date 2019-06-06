from RingFilter import RingFilter
from ContrasteImagem import ContrasteImagem

class PdsImagem:
    def __init__(self):
        continuar = True
        while(continuar):
            print('Menu')
            print('Parte II - Imagem')
            print('(1) Q1 - Filtrar a imagem "lena_rings.bmp" a fim para diminuir (ou remover) o efeito de ringing.')
            print('(2) Q1 - Filtrar a imagem "lena_rings.bmp" a fim para diminuir (ou remover) o efeito de ringing para um intervalo.')
            print('(3) Q2 - Contagem de regiões com diferentes texturas na imagem "alumgrns.bmp".')
            print('(4) Q3 - Melhorar a distinção dos números na imagem "dalton.bmp" para pessoas daltônicas.')
            print('(5) Q3 - Melhorar a distinção dos números na imagem "dalton.bmp" para pessoas daltônicas com Intervalo.')
            print('(6) Voltar.')
            print('(7) Sair')

            op = input('>> ')

            if op == '1':
                sigma = 0
            
                while(sigma <= 0):
                    sigma = round(float(input('Definir valor para sigma: ')),2)
                    if(sigma <= 0):
                        print('Insira um valor maior que a 0 (zero)')
                        
                self.efeitoRinging(sigma)
                
            elif op == '2':
                sigmaIni = 0
                sigmaFim = 0
                inc = 0
                
                while(sigmaIni <= 0):
                    sigmaIni = round(float(input('Definir valor inicial do intervalo (maior que zero): ')),2)
                    if(sigmaIni <= 0):
                        print('Insira um valor maior que 0 (zero)')

                while(sigmaFim <= sigmaIni):
                    sigmaFim = round(float(input('Definir valor final do intervalo (maior que o inicial): ')),2)
                    if(sigmaFim <= sigmaIni):
                        print('Insira um valor maior que ' + str(sigmaIni))

                while(inc <= 0):
                    inc = round(float(input('Definir valor de incremento (maior que zero): ')),2)
                    if(inc <= 0):
                        print('Insira um valor maior que 0 (zero)')
                    
                self.efeitoRingingIntervalo(sigmaIni, sigmaFim, inc)
                
            elif op == '3':
                self.contagemTextura()
                
            elif op == '4':
                indiceContraste = 0
                RGB = ''
                
                while(indiceContraste <= 0):
                    indiceContraste = round(float(input('Definir valor de contraste (maior que zero): ')),2)
                    if(indiceContraste <= 0):
                        print('Insira um valor maior que 0 (zero)')

                while(RGB != 'r' and RGB != 'R' and RGB != 'g' and RGB != 'G' and RGB != 'B' and RGB != 'B'):
                    RGB = input('Eixo RGB (R - vermelho, G - verde, B - blue): ')
                    if(RGB != 'r' and RGB != 'R' and RGB != 'g' and RGB != 'G' and RGB != 'B' and RGB != 'B'):
                        print('Opçao invalida')
                        
                self.contrasteImagem(RGB, indiceContraste)
                
            elif op == '5':
                sigmaIni = 0
                sigmaFim = 0
                inc = 0
                RGB = ''
                
                while(sigmaIni <= 0):
                    sigmaIni = round(float(input('Definir valor inicial do intervalo (maior que zero): ')),2)
                    if(sigmaIni <= 0):
                        print('Insira um valor maior que 0 (zero)')

                while(sigmaFim <= sigmaIni):
                    sigmaFim = round(float(input('Definir valor final do intervalo (maior que o inicial): ')),2)
                    if(sigmaFim <= sigmaIni):
                        print('Insira um valor maior que ' + str(sigmaIni))

                while(inc <= 0):
                    inc = round(float(input('Definir valor de incremento (maior que zero): ')),2)
                    if(inc <= 0):
                        print('Insira um valor maior que 0 (zero)')

                while(RGB != 'r' and RGB != 'R' and RGB != 'g' and RGB != 'G' and RGB != 'B' and RGB != 'b'):
                    RGB = input('Eixo RGB (R - vermelho, G - verde, B - blue): ')
                    if(RGB != 'r' and RGB != 'R' and RGB != 'g' and RGB != 'G' and RGB != 'B' and RGB != 'b'):
                        print('Opçao invalida')
                        
                self.contrasteImagemIntervalo(RGB, sigmaIni, sigmaFim, inc)

            elif op == '6':
                continuar = False
            
            elif op == '7':
                exit()

            else:
                print('Opção invalida')

    ## Parte II - Questão 1
    def efeitoRinging(self, sigma):
        ringFilter = RingFilter()
        ringFilter.aplicarFiltroRinging(sigma)
        print('Execução finalizada...')

    ## Parte II - Questão 1
    def efeitoRingingIntervalo(self, sigmaIni, sigmaFim, inc):
        sigma = sigmaIni
        ringFilter = RingFilter()
        
        while(sigma <= sigmaFim):
            ringFilter.aplicarFiltroRinging(sigma)
            sigma += inc

        print('Execução finalizada...')

    ## Parte II - Questão 2
    def contagemTextura(self):
        print('Em construçao')

    ## Parte II - Questão 3
    def contrasteImagem(self, RGB, indiceContraste):
        imgContraste = ContrasteImagem()
        imgContraste.aplicarContraste(RGB, indiceContraste)
        print('Execução finalizada...')

    ## Parte II - Questão 3
    def contrasteImagemIntervalo(self, RGB, iniIntervalo, fimIntervalo, inc):
        indice = iniIntervalo
        imgContraste = ContrasteImagem()

        while(indice <= fimIntervalo):
            imgContraste.aplicarContraste(RGB, indice)
            indice += inc
            
        print('Execução finalizada...')
