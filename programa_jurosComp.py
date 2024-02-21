cap = float(input('Digite o valor do capital: '))
temp = float(input('Digite o tempo ao mês: '))
ju = float(input('Digite a taxa de juros ao mês: '))
juros = 1 + ju / 100
capital = juros ** temp
M = cap * capital
print('O valor do seus juros compostos é: {:.3f}'.format(M))

