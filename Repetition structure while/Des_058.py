from random import randint
from time import sleep

print('=-'*25)
print('DIGITE UM NÚMERO DE 0 E A 10 E TENTE ME DERROTAR!')
print('=-'*25)
n_pess = ''
pc = randint(0, 10)
c = 0
x =''

while n_pess != pc:
    n_pess = int(input('{}Digite aqui > ' .format(x)))
    c += 1
    if n_pess > pc:
        x = 'Menos... '
    elif n_pess < pc:
        x = 'Mais... '

print('N-NÃO')
sleep(1)
print('NÃO É POSSÍ...')
sleep(1)
print('NÃO É POSSÍVEL...')
sleep(1)
print('ARRRRGHH')
sleep(0.5)
print('VOCÊ CONSEGUIU ME DERROTAR!')
print('Você precisou de {} tentativas para conseguir!' .format(c))
