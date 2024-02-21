import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

#primeiramente use o comando 'import' para importar a biblioteca de matemática 'math'#
#o comando 'sqrt' é um comando da biblioteca de raiz quadrada#
#O comando 'math.ceil' serve para arredondar o número para mais.#
#exemplo: raiz quadrada de 29 é 5.39 mas, se usar o comando 'ceil' ele arredonda para 6#
