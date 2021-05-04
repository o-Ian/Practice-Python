dados = {}
gols = []
v = 0
dados['nome'] = input('Nome do jogador: ')
n = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, n):
    g = (int(input(f'Quantas gols na partida {c+1}? ')))
    gols.append(g)
dados['total_gols'] = sum(gols)
dados['gols'] = gols
for cont in gols:
    print(f'Na partida {v+1} {dados["nome"]} fez {cont} gols.')
    v += 1
print(f'Foi um total de {dados["total_gols"]} gols em {n} partidas.')
