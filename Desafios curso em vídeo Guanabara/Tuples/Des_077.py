palavras = ('Celular', 'Monitor', 'Computador', 'Garrafa', 'Fone')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos as vogais: ', end='')
    for letras in c:
        if letras in 'aeiou':
            print(f'{letras} ', end='')
