from random import randint


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(0, 100)
        lista.append(n)
        print(n, end=' ')
    print()


def somaPar(lista):
    p = 0
    print(f'Somando os valores pares de {lista}, temos', end=' ')
    for c in lista:
        if c % 2 == 0:
            p += c
    print(p, end='.')


p = []
sorteia(p)
somaPar(p)
