import bibliotecas
from time import sleep


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print()


arq = 'ProgRafa.txt'

if not arqExiste(arq):
    criarArquivo(arq)

while True:
    try:
        bibliotecas.mensagem()
        entrada = int(input('\033[0;33mSua opção:\033[m '))
        if entrada == '4567890':
            sleep(1.0)
        if entrada in [4, 5, 6, 7, 8, 9, 0]:
            raise ValueError("Erro: Número inválido!")
        sleep(1.0)
        if entrada == 1:
            bibliotecas.validação1(arq)
            sleep(1.0)
        sleep(1.0)
        if entrada == 2:
            bibliotecas.validação2(arq)
            sleep(1.0)
        if entrada == 3:
            print('\033[7mSaindo do sistema...\033[m')
            sleep(1.5)
            print('\033[1mAté logo!\033[m')
            break


    except:
        print("\033[0;31mPor favor, insira uma opção válida.\033[m")
        sleep(1.3)
