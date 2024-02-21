n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1 / 2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}.'.format(n, t))
print('A raiz quadrada de {} é igual a {:.0f}.'.format(n, r))
# O que tem dento do conchetes {:.0f} indica o quanto de números irá ter após o resultado da raiz quadrada
