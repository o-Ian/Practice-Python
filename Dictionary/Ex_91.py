from random import randint
from operator import itemgetter
cont = 1
jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
for k, v in jogadores.items():
    print(f'O {k} tirou {v}.')
print('O ranking dos jogadores é: ')
valores = sorted(jogadores.values(), reverse=True)
lista = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, c in enumerate(lista):
    print(f'{i+1}° lugar: {c[0]} tirou {c[1]}')

    '''for c in valores:
    for k, v in jogadores.items():
        if c == v and k not in lista:
            print(f'{cont}° lugar: {k} com {v}.')
            lista.append(k)
            cont += 1'''