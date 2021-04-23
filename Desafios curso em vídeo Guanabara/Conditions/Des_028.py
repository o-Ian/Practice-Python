from random import randint
from time import sleep
nc = randint(0, 5)
print('-='*30)
print('Vou pensar em um número e você vai ter que adivinhar!')
print('-='*30)
np = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1.5)
if np == nc:
    print('PARABÉNS, VOCÊ CONSEGUIU ME DERROTAR *_*')
else:
    print('Eu pensei no número {}!Hahahahahaa você PERDEU!' .format(nc))
