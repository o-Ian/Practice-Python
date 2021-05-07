r = ''
qntd = 0
soma = 0
while r != 'N':
    n = int(input('Digite um número inteiro: '))
    qntd += 1
    soma += n
    if qntd == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    r = input('Quer continuar? [S/N] > ') .upper()
print('A média entre os valores digitados foi {:.2f}' .format(soma/qntd))
print('Menor: {} Maior {}' .format(menor, maior))
