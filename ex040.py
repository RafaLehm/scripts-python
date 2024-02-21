from random import randint
from time import sleep
itens = ('\033[1;30;44mPedra\033[m', '\033[1;30;45mPapel\033[m', '\033[1;30;46mTesoura\033[m')
computador = randint(0, 2)
print('''Suas opções:
[0] \033[1;30;44mPEDRA\033[m
[1] \033[1;30;45mPAPEL\033[m
[2] \033[1;30;46mTESOURA\033[m ''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-'* 10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=-'* 10)
if computador == 0:
    if jogador == 0:
        print('\033[1;30;43mEMPATE\033[m')
    elif jogador == 1:
        print('\033[1;30;42mJOGADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[1;30;41mCOMPUTADOR VENCE\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('\033[1;30;41mCOMPUTADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[1;30;43mEMPATE\033[m')
    elif jogador == 2:
        print('\033[1;30;42mJOGADOR VENCE\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('\033[1;30;42mJOGADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[1;30;41mCOMPUTADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[1;30;43mEMPATE\033[m')
    else:
        print('JOGADA INVÁLIDA')



