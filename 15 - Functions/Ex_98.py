from time import sleep


def contagem(begin, end, passo):
    cont = 0
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = passo * -1
    print(f'Contagem de {begin} até {end} de {passo} em {passo}')
    if end < 0:
        cont += 1
        if begin < 0:
            cont += 1
    if begin > end:
        begin *= -1
        end *= -1

    for c in range(begin, end+1, passo):
        if cont == 1:
            if c < 0:
                c = abs(c)
            else:
                c = c * (-1)
            print(c, end=' ')
        elif cont == 2:
            print(c, end=' ')
        else:
            print(abs(c), end=' ')

        sleep(0.3)
    print('FIM!')
    print('-='*25)


print('-='*25)
contagem(1, 10, 1)
contagem(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
