dados = []
jogador = {}
gols = []
cont = 0
while True:
    jogador['nome'] = input('Nome do jogador: ')
    n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, n):
        gols.append(int(input(f'Quantas gols na partida {c+1}? ')))
    jogador['cod'] = cont
    cont += 1
    jogador['gols'] = gols.copy()
    dados.append(jogador.copy())
    gols.clear()
    r = input('Quer continuar? [S/N]: ') .upper()[0]
    print('-'*28)
    if r in 'N':
        break
print(f'{"cod":<4} {"nome":<10} {"gols":<10}{"total de gols":>10}')
for k, v in enumerate(dados):
    print(f'{dados[k]["cod"]:<4} {dados[k]["nome"]:<10} {str(dados[k]["gols"]):<20}{sum(dados[k]["gols"]):<20}')

r = 0
print('=-'*20)
while True:
    r = int(input('Mostrar dados de qual jogador? '))
    if r == 999:
        break
    print('-'*30)
    print(f'-LEVANTAMENTO DO JOGADOR {dados[r]["nome"]}')
    for n, c in enumerate(dados[r]["gols"]):
        print(f'Na partida {n+1} fez {c} gols')
