from RingFilter import RingFilter
from ContrasteImagem import ContrasteImagem

class PdsImagem:
    def __init__(self):
        invalOP = True

        while(invalOP):
            ret = False
        
            print('Menu')
            print('Parte II - Imagem')
            print('(1) Filtrar a imagem "lena_rings.bmp" a fim para diminuir (ou remover) o efeito de ringing.')
            print('(2) Contagem de regiões com diferentes texturas na imagem "alumgrns.bmp".')
            print('(3) Melhorar a distinção dos números na imagem "dalton.bmp" para pessoas daltônicas.')

            op = input()

            if op == '1':
                while (ret == False):
                    ret = self.efeitoRinging()
                invalOP = False
            elif op == '2':
                while(ret == False):
                    ret = self.contagemTextura()
                invalOP = False
            elif op == '3':
                while(ret == False):
                    ret = self.contrasteImagem()
                invalOP = False
            else:
                print('Opção invalida')
                invalOP = True

    ## Parte II - Questão 1
    def efeitoRinging(self):
        print('Definir valor para sigma, S|N?')
        op = input()
        sigmaIni = 0
        sigmaFim = 0
        inc = 0
        
        if (op == 's' or op == 'S'):
            while(sigmaIni <= 0):
                print('Valor inicial de Sigma?')
                sigmaIni = round(float(input()),2)
                if(sigmaIni <= 0):
                    print('Insira um valor maior que 0 (zero)')

            while (sigmaFim < sigmaIni):
                print('Valor final de Sigma?')
                sigmaFim = round(float(input()),2)
                if(sigmaFim < sigmaIni):
                    print('Insira um valor maior que '+ str(sigmaIni))

            while (inc <= 0):
                print('Incremento?')
                inc = round(float(input()),2)
                if(inc <= 0):
                    print('Insira um valor maior que 0 (zero)')
                    
        elif (op != 'n' and op != 'N'):
            print('Opção inválida')
            return False
        
        else:
            sigmaIni = 0.1
            sigmaFim = 2.5
            inc = 0.1
            
        print('Iniciando aplicação de filtro...')
        ringFilter = RingFilter()
        sigma = sigmaIni
        while(sigma <= sigmaFim):
            ringFilter.applyRingFilterSave(sigma)
            sigma += inc
        print('Execução finalizada...')
        return True

    ## Parte II - Questão 2
    def contagemTextura(self):
        print('Em construçao')
        return True

    ## Parte II - Questão 3
    def contrasteImagem(self):
        return True
            
