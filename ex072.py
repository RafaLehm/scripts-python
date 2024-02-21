def conta(a, b):
    c = a * b
    print(f'A área de um terreno {a}x{b} é de {c}m²')


def mensagem():
    print('Controle de Terrenos')
    print('-' * 20)


mensagem()
conta(float(input('Largura (m): ')), float(input('Comprimento (m): ')))