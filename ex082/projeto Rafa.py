from time import sleep

def mensagem():
    print('-' * 30)
    print('       MENU PRINCIPAL')
    print('-' * 30)
    print('''\033[0;33m1 -\033[m \033[0;34mVer pessoas cadastradas\033[m
\033[0;33m2 -\033[m \033[0;34mCadastrar novas pessoas\033[m
\033[0;33m3 -\033[m \033[0;34mSair do sistema\033[m''')
    print('-' * 30)


def validação1(nome):
    try:
        with open(nome, 'rt') as a:
            print('-' * 30)
            print('       PESSOAS CADASTRADAS')
            print('-' * 30)
            for linha in a:
                nome, idade = linha.strip().split(', ')
                print(f'{nome:<30} {idade:>5} anos')
    except FileNotFoundError:
        print('Arquivo não encontrado!')
    except:
        print('Erro ao ler o arquivo!')


def validação2(nome_arquivo):
    print('-' * 30)
    print('   Cadastro de Novas Pessoas')
    print('-' * 30)

    try:
        with open(nome_arquivo, 'a') as arquivo:
            while True:
                nome = input("Digite o nome da pessoa (ou digite \033[0;34m'sair'\033[m para sair): ")
                if nome.lower() == 'sair':
                    break
                elif any(char.isdigit() for char in nome):
                    print('\033[0;31mNome não pode conter números. Tente novamente!\033[m')
                    continue

                while True:
                    idade = input("Digite a idade da pessoa (ou digite \033[0;34m'sair'\033[m para sair): ")
                    if idade.lower() == 'sair':
                        break
                    try:
                        idade = int(idade)
                        if idade < 0:
                            raise ValueError('A idade não pode ser negativa')
                        arquivo.write(nome + ', ' + str(idade) + '\n')
                        print(f'\033[0;33m{nome}\033[m cadastrado com sucesso!')
                        break
                    except:
                        print('\033[0;31mPor favor, insira uma opção válida.\033[m')

    except Exception as e:
        print('Erro ao cadastrar pessoa:', e)

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
