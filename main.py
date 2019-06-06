from PDS_Imagem import PdsImagem

if __name__ == "__main__":

    continuar = True
    
    while(continuar):
        print('Projeto de Processamento Digital de Sinais - 2019.1')
        print('Selecione:')
        print('1 - Sinais')
        print('2 - Imagem')
        print('3 - Vídeo')
        print('4 - Voz e Som')
        print('5 - Sair')

        op = input('>> ')

        if op == '1':
            print('\nEm implementação...\n')
        elif op == '2':
            PdsImagem()
        elif op == '3':
            print('\nEm implementação...\n')
        elif op == '4':
            print('\nEm implementação...\n')
        elif op == '5':
            continuar = False
        else:
            print('Opcao invalida...\n')
