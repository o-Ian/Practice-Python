from random import randint

n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram: ', end='')
for c in n:
    print(f'{c} ', end='')
print(f'\nO maior número sorteado é {max(n)}')
print(f'O menor número sorteado é {min(n)}')
