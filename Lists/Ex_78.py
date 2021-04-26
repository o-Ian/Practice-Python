valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

print(f'O menor valor digitado foi {min(valores)} nas posições ', end='')
for i, c in enumerate(valores):
    if c == min(valores):
        print(f'{i}... ', end='')
print(f'\nO maior valor digitado foi {max(valores)} nas posições ', end='')
for i, c in enumerate(valores):
    if c == max(valores):
        print(f'{i}... ', end='')
