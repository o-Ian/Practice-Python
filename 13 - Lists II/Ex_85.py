numeros = [[], []]
for c in range(0, 7):
    n = (int(input('Digite um número: ')))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

numeros[0].sort()
print(f'Os números pares são: {numeros[0]}')
numeros[1].sort()
print(f'Os números ímpares são: {numeros[1]}')
