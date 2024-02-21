from random import randint
computador = randint(0, 5) # faz o computador "pensar"
print("-=-" * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensei? ')) # jogador tenta adivinhar
if jogador == computador:
    print('Parabéns! você conseguiu me vencer')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))