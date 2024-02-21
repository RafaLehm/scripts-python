from datetime import date
dados = {}
ano = date.today().year
dados['nome'] = str(input('Nome: '))
dados['Nascimento'] = int(input('Ano de nascimento: '))
dados['CLT'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['CLT'] == 0:
    print(f'- nome do cadastrado: {dados["nome"]}')
    print(f'- idade do cadastrado: {ano - dados["Nascimento"]} anos')
    print(f'- Número da CLT: {dados["CLT"]}')
    print('-=' * 25)
else:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    print(f'- nome do cadastrado: {dados["nome"]}')
    print(f'- idade do cadastrado: {ano - dados["Nascimento"]} anos')
    print(f'- Número da CLT: {dados["CLT"]}')
    print(f'- Ano em que foi contratado: {dados["Contratação"]}')
    print(f'- Salário do cadastrado: {dados["Salário"]:.2f}')
    print(f'- Idade da aposentadoria do cadastrado: {dados["Contratação"] - dados["Nascimento"] + 35} anos')
    print('-=' * 25)

