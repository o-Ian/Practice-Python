matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = soma3 = scout = 0

for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite o valor para a linha {l+1} e coluna {c+1}: '))
        matriz[l][c] = n
        if n % 2 == 0:
            par += n

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}] ', end='')
    print()

print(f'A soma de todos os valores pares é: {par}')
for l in range(0, 3):
    scout += matriz[l][2]
print(f'A soma dos valores da coluna 3 é: {scout} ')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
