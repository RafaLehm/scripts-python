casa = (float(input('Valor da casa: R$ ')))
salário = (float(input('Salário do comprador: R$ ')))
anos = (int(input('Quantos anos de financiamento? ')))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
print('-=-' * 25)
if prestação <= mínimo:
 print('Empréstimo pode ser \033[0;42mCONCEDIDO\033[m!')
else:
 print('Empréstimo \033[0;41mNEGADO\033[m!')
print('-=-' * 25)

