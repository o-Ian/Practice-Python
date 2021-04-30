dados = []
lista = []
n = 0
while True:
    dados.append(input('Nome: '))
    dados.append(int(input('Nota 1: ')))
    dados.append(int(input('Nota 2: ')))
    lista.append(dados[:])
    dados.clear()
    n += 1
    resp = input('Quer continuar? [S/N]: ')
    if resp in 'Nn':
        break
print('=-'*30)
print('No   Nome')
for n in range(0, n):
    print(f'{n:<5}')

for p in lista:
    print(f'{p[0]}')
