while True:
    try:
        inteiro = int(input('Digite um número inteiro: '))
        break
    except:
        print('\033[0;31mERRO: Por favor, digite um número inteiro válido.\033[m')


while True:
    try:
        real = float(input('Digite um número real: '))
        print(f'O valor inteiro digitado foi {inteiro} e o valor real foi {real}')
        break
    except:
        print('\033[0;31mERRO: Por favor, digite um número real válido.\033[m')


