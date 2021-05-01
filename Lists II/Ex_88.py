from random import randint
lista = []
jogo = []
n = int(input('Quantos jogos você quer sortear? '))
for c in range(0, n):
    for cont in range(0, 6):
        num = randint(1, 60)
        while True:
            while num in jogo:
                num = randint(1, 60)
            if num not in jogo:
                jogo.append(num)
                break
    lista.append(jogo[:])
    lista[c].sort()
    print(f'Jogo {c+1}: {lista[c]}')
    jogo.clear()
