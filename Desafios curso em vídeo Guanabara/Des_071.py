n = int(input('Quantos reais você quer sacar? R$'))
ced50 = ced20 = ced10 = ced1 = c = 0

if (n // 50) >= 1:
    ced50 = n // 50
    total = n - (50 * ced50)
if (total // 20) >= 1:
    ced20 = total // 20
    total = total - (20 * ced20)
if (total // 10) >= 1:
    ced10 = total // 10
    total = total - (10 * ced10)
if (total // 1) >= 1:
    ced1 = total // 1
    total = total - (1 * ced1)

if ced50 >= 1:
    print(f'Total de {ced50} cédulas de R$50')
if ced20 >= 1:
    print(f'Total de {ced20} cédulas de R$20')
if ced10 >= 1:
    print(f'Total de {ced10} cédulas de R$10')
if ced1 >= 1:
    print(f'Total de {ced1} cédulas de R$1')
