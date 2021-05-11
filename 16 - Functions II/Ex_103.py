def ficha(nome='', gols=''):
    if nome == '':
        nome = '<desconhecido>'
    if not gols.isnumeric():
        gols = 0

    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome = input('Digite o nome do jogador: ')
gols = input('Número de gols: ')
ficha(nome, gols)
