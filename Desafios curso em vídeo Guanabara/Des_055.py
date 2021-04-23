maior = 0
menor = 0
for c in range(1, 6):
    p = float(input('Digite o peso da pessoa {}: ' .format(c)))
    if p > maior:
        maior = p
        if c == 1:
            menor = p
    elif p < menor:
        menor = p
print('O maior peso digitado foi {}kg e o menor foi {}kg' .format(maior, menor))
