num = []
imp = []
par = []
while True:
    num.append(int(input('Digite um número: ')))
    r = input('Você quer continuar? [S/N]: ') .strip().upper()[0]
    if r in 'N':
        break

print(f'Todos os números digitados: {num}')
for c in num:
    if c % 2 == 0:
        par.append(c)
    else:
        imp.append(c)
print(f'Os números pares digitados: {par}')
print(f'Os números ímpares digitados: {imp}')
