pessoas = []
dados = []
while True:
    dados.append(input('Digite seu nome: '))
    dados.append(float(input('Digite seu peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    r = input('Quer continuar? [S/N]: ')
    if r in 'Nn':
        break
print(f'{len(pessoas)} pessoas foram cadastradas!')
pesado = 0
leve = 0
nome_pesado = nome_leve = ''
for c in pessoas:
    if pesado == 0 and leve == 0:
        leve = c[1]
        pesado = c[1]
        nome_pesado = c[0]
        nome_leve = c[0]
    elif c[1] >= pesado:
        pesado = c[1]
        nome_pesado = c[0]
    elif c[1] <= leve:
        leve = c[1]
        nome_leve = c[0]
print(f'O maior peso foi de {pesado}kg. Peso de ', end='')
for cont in pessoas:
    if cont[1] == pesado:
        print(f'[{cont[0]}] ', end='')
print(f'\nO menor peso foi de {leve}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == leve:
        print(f'[{p[0] }] ', end='')
