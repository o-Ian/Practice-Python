sumIdade = 0
velho = 0
nome_velho = ''
novo = 0
qtnd_20 = 0
for c in range(1, 5):
    print('-------- {}ª pessoa --------' .format(c))
    nome = str(input('Digite o nome da pessoa {}: ' .format(c))) .strip()
    idade = int(input('Digite em números a idade de {}: '.format(nome)))
    sexo = input('Você é de qual sexo?\n[ M ] para masculino\n[ F ] para feminino\nDigite: ' .format(c)) .upper().strip()
    if sexo == 'M' or sexo == 'F':
        sumIdade += idade
        if sexo == 'M':
            if idade > velho:
                velho = idade
                nome_velho = nome
        else:
            if idade < 20:
                qtnd_20 += 1

    else:
        print('\033[1;41mDigite M ou F!\033[m')
        break

if sexo == 'M' or sexo == 'F':
    medIdade = sumIdade/c
    print('A média de idade de todo o grupo é de {:.1f} anos.' .format(medIdade))
    print('O nome do homem mais velho é {} com {} anos.' .format(nome_velho, velho))
    print('Há {} mulheres com menos de 20 anos no grupo.' .format(qtnd_20))
else:
    ''
