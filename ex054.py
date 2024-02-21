num = 0
while True:
    print('---' * 13)
    num = int(input('Para sair digite "999"'
                    '\nQuer ver a tabuada de qual valor? '))
    if num == 999:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
print("-" * 39)
print('Programa finalizado. Volte Sempre!')


