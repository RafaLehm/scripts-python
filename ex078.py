"""def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
        return valor


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')"""


# O código acima é do gustavo guanabara, e infelizmente não funcionou.
def leiaint(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')