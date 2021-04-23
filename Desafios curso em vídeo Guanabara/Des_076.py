lista = ('Leite', 3.5, 'Chocolate', 9.25, 'Macarrão', 6.5, 'Lápis', 1.25, 'Caderno', 15.98)
print('-'*40)
print('{:^40}' .format('LISTAGEM DE PREÇO'))
print('-'*40)
for c in lista:
    if c == str(c):
        print(f'{c:.<30}', end='')
    else:
        print(f'R${c:6}')
