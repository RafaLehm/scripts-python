nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if 7 > média >=5:
    print('O aluno está em \033[43mRECUPERAÇÃO\033[m.')
elif média < 5:
    print('O aluno está \033[41mREPROVADO\033[m')
elif média >= 7:
    print('O aluno está \033[42mAPROVADO\033[m.')