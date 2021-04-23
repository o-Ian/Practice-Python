maior = menor = homem = mulher_20 = 0
while True:
    i = int(input('Digite a idade: '))
    if i > 18:
        maior += 1
    else:
        menor += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo dessa pessoa [M/F]: ')) .strip().upper()[0]
    if sexo == 'M':
        homem += 1
    elif sexo == 'F':
        if i < 20:
            mulher_20 += 1

    r = ' '
    while r != 'S' and r != 'N':
        r = input('Quer continuar? [S/N]: ') .strip().upper()[0]
    if r == 'N':
        break

print(f'{maior} pessoas são maiores de 18 anos.\n{homem} homens foram cadastrados.'
      f'\n{mulher_20} mulheres tem menos de 20 anos.')
