def aumento(n=0):
    '''
    -> calcula ajustes de preços
    :param aumento: aumenta em 10% o valor especificado
    :param dobro: Dobra o valor especificado
    :param metade: mostra metade do valor especificado
    :param dinheiro: mostra o cifrão R$ da respectiva moeda. Também muda o ponto pela vírgula
    :return: mostra o valor já reajustado
    '''
    return n * 1.10


def dobro(n=0):
    return n * 2


def metade(n=0):
    return n / 2


def dinheiro(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0):
    print('-' * 45)
    print('Resumo do valor'.center(30))
    print('-' * 45)
    print(f'Preço analisado {dinheiro(n)}')
    print(f'Metade do preço {dinheiro(metade(n))}')
    print(f'Dobro do preço {dinheiro(dobro(n))}')
    print(f'Com 10% de taxa, o acréscimo foi de {dinheiro(aumento(n))}')
    print('-' * 45)
