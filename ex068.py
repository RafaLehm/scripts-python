aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    print('O aluno foi Aprovado. Parabéns!')
elif aluno['média'] >= 5:
    print('O aluno está em recuperação.')
else:
    print('O aluno reprovou. Tente novamente no ano que vem!')