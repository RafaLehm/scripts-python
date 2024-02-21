import pygame
import emoji
from time import sleep
for c in range(9+1, 0, -1 ):
    sleep(1)
    print(c)
print(emoji.emojize(':clinking_glasses: :collision:'))
for d in range(1):
    print('Feliz Ano novo!!!')
    sleep(1)
    print('Boas Festas!!!')
pygame.init()
pygame.mixer.music.load('ex041.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()