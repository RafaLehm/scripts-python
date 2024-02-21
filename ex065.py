lista = []
pares = []
ímpares = []
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar [S/N] '))
    if resposta in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('=-' * 25)
print(f'A lista completa é {lista}')
print(f'Os valores pares são {pares}')
print(f'Os valores ímpares são {[ímpares]}')

