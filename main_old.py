from pdsimagem import PdsImagem

if __name__ == "__main__":
    print('Selecione: ')
    print('(1) Sinais')
    print('(2) Imagem')
    print('(3) Video')
    print('(4) Voz e Som')

    op = input()

    if op == '2':
        img = PdsImagem()
        print (img)
    else:
        print('Opção inválida!')
        
