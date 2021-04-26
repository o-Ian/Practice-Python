num = []
resp = ''
while True:
    n = (int(input('Digite um número: ')))
    if n not in num:
        print('Valor adicionado com sucesso...')
        num.append(n)
    else:
        print('Valor duplicado! Não irei adicionar...')
    resp = input('Quer continuar? [S/N]: ') .upper().strip()[0]
    if resp in 'N':
        break
print('-=' * 40)
print(f'Você digitou os números {sorted(num)}')
