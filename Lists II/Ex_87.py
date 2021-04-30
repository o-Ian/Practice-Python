matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = soma3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite o valor para a linha {l} e coluna {c}: '))
        matriz[l][c] = n
        if n % 2 == 0:
            par += n
            if matriz[c] == 2:
                soma3 += n
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[c][l]:^5}] ', end='')
    print()
print(f'A soma de todos os valores pares é: {par}')
print(f'A soma dos valores da coluna 3 é: {soma3} ')
