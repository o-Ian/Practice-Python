from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da pessoa {}: ' .format(c)))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Há {} pessoas menores e {} pessoas maiores.' .format(menor, maior))
